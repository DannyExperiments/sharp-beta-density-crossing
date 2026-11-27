# Reproducibility

Run from the repository root using Python 3.9 or newer. The replay uses the Python standard library and exact fractions.

```sh
python3 -I scripts/verify_repository.py
python3 -I verification/src/replay.py
```

Compare with [the checked log](verification/logs/replay.txt). The exact replay checks the trial density inequalities and crossing brackets by rational arithmetic. The illustrated curves are rounded for display. [PDF build](paper/BUILD.md) · [Visualization build](visualization/README.md)
