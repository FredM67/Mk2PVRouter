"""Check every part reference cited in the docs against the KiCad PCBs.

For each board: ref -> (value, smd/tht/mixed, footprint). For each doc line citing refs:
- ref absent from the page's board -> MISSING
- "REF (value)" or "REF : value" where value differs from KiCad -> VALUE
- SMD-only ref cited on a line about soldering / joints / user assembly -> SMD-SOLDER (manual review)
Usage: python refcheck.py <docs content dir> <kicad repo> [--ref GITREF] [FILE ...]
Reads the PCBs as committed at origin/main (git show) unless --ref is given.
FILE: limit the report to these .rst files (paths relative to the content dir).
Phase names (L1-L3) and Arduino pins (D2-D13) also match the ref pattern: ignore those lines.
"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
gitref = "origin/main"
if "--ref" in args:
    i = args.index("--ref")
    gitref = args[i + 1]
    del args[i:i + 2]
content, kicad, only = pathlib.Path(args[0]), pathlib.Path(args[1]), {a.replace("\\", "/") for a in args[2:]}
BOARDS = {
    "main": "mainboard/3phaseDiverter.kicad_pcb",
    "out": "output_stage/Output_stage.kicad_pcb",
    "ind": "Indicator/Indicator.kicad_pcb",
    "c6": "expansion_boards/mk2Wifi-C6/mk2Wifi-C6.kicad_pcb",
}


def parts(rel):
    text = subprocess.run(["git", "-C", str(kicad), "show", f"{gitref}:{rel}"], capture_output=True, check=True).stdout.decode("utf-8")
    out, ref, val, fp, kinds = {}, None, None, None, set()
    def flush():
        if ref:
            kind = "mixed" if len(kinds) > 1 else (kinds.pop() if kinds else "?")
            out[ref] = (val, kind, fp)
    for line in text.splitlines(keepends=True):
        if line.startswith("\t(footprint \""):
            flush()
            ref, val, kinds = None, None, set()
            fp = line.split('"')[1]
        elif '(property "Reference" "' in line and ref is None:
            ref = line.split('"')[3]
        elif '(property "Value" "' in line and val is None:
            val = line.split('"')[3]
        elif re.match(r'\t\t\(pad "', line):
            kinds.add("smd" if " smd " in line else "tht" if "thru_hole" in line else "other")
    flush()
    return out


db = {k: parts(p) for k, p in BOARDS.items()}
REF = re.compile(r"(?<![\w/#-])((?:GDT|JP|TP|FS|GM|RV|TR|PS|FL|CN|SW|IC|LED|R|C|D|U|J|L|Q|X)\d{1,2})(?![\w’'])")
SOLDER = re.compile(r"soud|joint|brasure|fer à|étain|pont de soudure|à souder", re.I)


def board_of(rel):
    s = str(rel).replace("\\", "/")
    if s.startswith("etage-sortie/carte-indicateur"):
        return "ind"
    if s.startswith("etage-sortie/"):
        return "out"
    if s.startswith("mk2wifi/") or "mk2wifi" in s:
        return "c6"
    return "main"


for path in sorted(content.rglob("*.rst")):
    rel = path.relative_to(content)
    if any(p.startswith("_") for p in rel.parts):
        continue
    if only and str(rel).replace("\\", "/") not in only:
        continue
    b = board_of(rel)
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for m in REF.finditer(line):
            ref = m.group(1)
            info = db[b].get(ref)
            others = [k for k in db if k != b and ref in db[k]]
            if info is None:
                # digital pins D2..D13 and CT1..3 are not parts; only flag if no other board has it
                if re.fullmatch(r"D\d{1,2}", ref) and not re.search(rf"{ref}\s*\(", line):
                    continue
                print(f"MISSING  {rel}:{n} [{b}] {ref} (on: {','.join(others) or '-'}) | {line.strip()[:150]}")
                continue
            val, kind, fp = info
            tail = line[m.end():m.end() + 40]
            mv = re.match(r"\s*\(([^)]{2,30})\)", tail) or re.match(r"\s*[:=]\s*([\w.,µΩ%/-]{2,20})", tail)
            if mv:
                cited = mv.group(1).replace(" ", " ").strip()
                norm = lambda s: re.sub(r"[\s Ωohm]", "", s.lower()).replace(",", ".")
                if val and norm(val)[:4] not in norm(cited) and norm(cited)[:4] not in norm(val):
                    print(f"VALUE?   {rel}:{n} [{b}] {ref} cited '{cited}' kicad '{val}' | {line.strip()[:150]}")
            if kind == "smd" and SOLDER.search(line):
                print(f"SMD-SOLDER {rel}:{n} [{b}] {ref} ({val}, SMD) | {line.strip()[:150]}")
