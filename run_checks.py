#!/usr/bin/env python3
"""Verify ESM archive integrity, reproduce exact outputs, compare with saved results."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).resolve().parent
SRC = BASE / "supplement"
OUT = BASE / "reproduced"

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert sys.flags.optimize == 0, "Never run with -O (assertions are required)"
    lines = (SRC / "SHA256SUMS.txt").read_text().splitlines()
    for line in lines:
        expected, name = line.split(maxsplit=1)
        p = SRC / name.strip()
        if sha256(p) != expected:
            raise AssertionError(f"Original archived checksum mismatch: {name}")
    OUT.mkdir(exist_ok=True)
    for script, reference, output in (
        ("verify_publication.py", "expected_results.json", "publication.json"),
        ("verify_historical_counts.py", "historical_count_arithmetic.json", "historical.json"),
    ):
        res = subprocess.run([sys.executable, str(SRC / script)],
                             check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             cwd=SRC, env={**os.environ, "PYTHONOPTIMIZE": "0"})
        got = json.loads(res.stdout)
        expected = json.loads((SRC / reference).read_text())
        if got != expected:
            raise AssertionError(f"Reproduced JSON differs from reference for {script}")
        (OUT / output).write_text(json.dumps(got, indent=2, ensure_ascii=False) + "\n")
        print(f"PASS {script} -> {output} (exact JSON match)")
    print("PASS original archive member checksums")
    print("ALL CHECKS PASSED")

if __name__ == "__main__": main()
