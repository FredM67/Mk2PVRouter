"""Print the parts of a Mk2PVRouter board as they are in KiCad.

One line per footprint: ref, value, footprint, pad kinds (smd / thru_hole / both),
schematic flags (dnp, in_bom), and each pad with its net.

Usage:
  python kicad_parts.py <kicad repo> <board> [REF ...] [--ref GITREF | --worktree]
  Reads the files as committed at origin/main by default (git show), so a maintainer's
  uncommitted work in the checkout is ignored. --ref picks another commit/branch,
  --worktree reads the files on disk.
  board: main | out | ind | c6
  REF:   exact refs, or a prefix ending in * (e.g. JP* R1*)
  --net NAME: only parts with a pad on that net (repeatable), e.g. --net NEUTRAL --net Earth
Examples:
  python kicad_parts.py D:/Git/IoT/PVRouter-KiCad main U1 JP0 GND_LINK1
  python kicad_parts.py ../PVRouter-KiCad main 'GDT*' 'RV*'
"""
import io
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

BOARDS = {
    "main": "mainboard/3phaseDiverter",
    "out": "output_stage/Output_stage",
    "ind": "Indicator/Indicator",
    "c6": "expansion_boards/mk2Wifi-C6/mk2Wifi-C6",
}

import subprocess

args = sys.argv[1:]
nets = []
while "--net" in args:
    i = args.index("--net")
    nets.append(args[i + 1])
    del args[i:i + 2]
gitref = "origin/main"
if "--worktree" in args:
    args.remove("--worktree")
    gitref = None
if "--ref" in args:
    i = args.index("--ref")
    gitref = args[i + 1]
    del args[i:i + 2]
repo, board, want = pathlib.Path(args[0]), args[1], args[2:]
rel = BOARDS[board]


def read(suffix):
    if gitref:
        r = subprocess.run(["git", "-C", str(repo), "show", f"{gitref}:{rel}{suffix}"], capture_output=True)
        return r.stdout.decode("utf-8") if r.returncode == 0 else ""
    p = repo / (rel + suffix)
    return io.open(p, encoding="utf-8").read() if p.exists() else ""


pcb, sch = read(".kicad_pcb"), read(".kicad_sch")
if not pcb:
    sys.exit(f"cannot read {rel}.kicad_pcb at {gitref or 'worktree'}")
print(f"# {rel} @ {gitref or 'worktree (uncommitted changes included)'}")

flags = {}
for m in re.finditer(r'\(symbol\s*\(lib_id "[^"]*"(.*?)\(property "Reference" "([^"]+)"', sch, re.S):
    f = dict(re.findall(r"\((dnp|in_bom|on_board) (yes|no)\)", m.group(1)))
    flags[m.group(2)] = " ".join(f"{k}={v}" for k, v in f.items())


def wanted(ref):
    if not want:
        return True
    return any(ref == w or (w.endswith("*") and ref.startswith(w[:-1])) for w in want)


rows = []
for fp in re.split(r"\n\t\(footprint ", pcb)[1:]:
    ref = re.search(r'\(property "Reference" "([^"]+)"', fp).group(1)
    if not wanted(ref):
        continue
    val = re.search(r'\(property "Value" "([^"]+)"', fp).group(1)
    name = fp.split('"')[1].split(":")[-1]
    kinds, pads = set(), []
    for m in re.finditer(r'\(pad "([^"]*)" (\w+)(.*?)\n\t\t\)', fp, re.S):
        kinds.add({"smd": "smd", "thru_hole": "tht"}.get(m.group(2), m.group(2)))
        n = re.search(r'\(net (?:\d+ )?"([^"]*)"\)', m.group(3))
        pads.append(f"{m.group(1)}={n.group(1) if n else '-'}")
    if not pads:  # logos, silkscreen symbols
        continue
    if nets and not any(p.split("=", 1)[1] in nets for p in pads):
        continue
    kind = "+".join(sorted(kinds)) or "-"
    rows.append((ref, val, name, kind, flags.get(ref, ""), " ".join(dict.fromkeys(pads))))

key = lambda r: [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", r[0])]
for r in sorted(rows, key=key):
    print("\t".join(r))
missing = [w for w in want if not w.endswith("*") and w not in {r[0] for r in rows}]
for w in missing:
    print(f"{w}\tNOT ON THIS BOARD (no footprint in the PCB; check the schematic: {bool(re.search(rf'\"Reference\" \"{re.escape(w)}\"', sch))})")
