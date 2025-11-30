# RST Section Level Reference for Mk2PVRouter Documentation

## Standard Hierarchy Used in This Project

```rst
Document Title (Level 1)
=========================

Major Section (Level 2)
-----------------------

Subsection (Level 3)
~~~~~~~~~~~~~~~~~~~~

Sub-subsection (Level 4)
^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph (Level 5)
"""""""""""""""""""

Sub-paragraph (Level 6)
'''''''''''''''''''''''
```

## Quick Reference Table

| Level | Character | Usage Example                              |
|-------|-----------|-------------------------------------------|
| 1     | `=`       | Document/Chapter title (introduction.rst)|
| 2     | `-`       | Major sections (Recommandations...)       |
| 3     | `~`       | Subsections (Composants Polarisés)       |
| 4     | `^`       | Sub-subsections (Composants à Surveiller)|
| 5     | `"`       | Paragraphs (detailed procedures)         |
| 6     | `'`       | Sub-paragraphs (fine details)            |

## Extended 8-Level Hierarchy (Rarely Needed)

For very deep documentation structures:

```rst
######################
Document Title (Level 0) - with overline
######################

Major Part (Level 1) - with overline
********************

Chapter (Level 2)
=================

Section (Level 3)
-----------------

Subsection (Level 4)
~~~~~~~~~~~~~~~~~~~~

Sub-subsection (Level 5)
^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph (Level 6)
"""""""""""""""""""

Sub-paragraph (Level 7)
'''''''''''''''''''''''
```

## Important Rules

1. **Underline length**: Must be **at least** as long as the title text
2. **Consistency**: Use the same character for the same level throughout the entire documentation
3. **No skipping**: Don't skip levels (e.g., don't go from `=` directly to `~` without using `-`)
4. **Overlines** (optional): Only for top-level titles (Level 0-1), both overline and underline must match

## Common Mistakes Fixed

❌ **Wrong** - Using `'` for level 4:
```rst
Composants Polarisés
~~~~~~~~~~~~~~~~~~~~

Composants à Surveiller
'''''''''''''''''''''''  ← Too deep!
```

✅ **Correct** - Using `^` for level 4:
```rst
Composants Polarisés
~~~~~~~~~~~~~~~~~~~~

Composants à Surveiller
^^^^^^^^^^^^^^^^^^^^^^^  ← Correct!
```

## Verification

To check for title level inconsistencies:
```bash
make html 2>&1 | grep -i "title level inconsistent"
```

## Notes

- Sphinx maps RST sections to HTML `<h1>` through `<h6>`
- Levels deeper than 6 become `<p class="rubric">` in HTML
- The actual character doesn't matter to RST parser, but consistency matters for maintainability
- Alternative characters for additional levels: `+ . : ; , _ *`

## Last Updated

2025-11-30 - Fixed 6 instances where `'` was incorrectly used instead of `^` for level 4 headings
