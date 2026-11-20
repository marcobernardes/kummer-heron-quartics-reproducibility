# Exact finite certificates for fourteen-nodal Heron-type quartics

Reproducibility source and exact computational evidence accompanying the **unpublished manuscript**

> **Fourteen-nodal Heron-type quartics: exterior lattices, Brauer classes and explicit Kummer correspondences**  
> Marco Aurélio dos Santos Bernardes  
> Physics and Engineering Department, Taylor University, Upland, Indiana, USA

**Project status:** publication supplement prepared for *Research in the Mathematical Sciences* (Springer Nature). No journal acceptance, published article DOI, public repository URL, or Zenodo DOI is asserted here.

## What is in this repository

- `supplement/verify_publication.py` — fresh exact symbolic, finite-discriminant, incidence, and small elliptic-curve computations.
- `supplement/verify_historical_counts.py` — checks Frobenius arithmetic from **retained historical count inputs**, not an independent recount of the quartic over finite fields.
- `supplement/expected_results.json` and `supplement/historical_count_arithmetic.json` — reference outputs.
- `supplement/historical_data/` — two exact historical count datasets from the authenticated research record.
- `supplement/ADDITIONAL_CERTIFICATES.md` — mathematical interpretation and scope.
- `supplement/SHA256SUMS.txt` — original per-file checksums.
- `archived_submission_supplement/ESM_1_NR130.zip` — byte-for-byte copy of the exact NR130 journal supplement.
- `run_checks.py` — reproducible local runner and comparison against both reference JSON outputs.
- `CITATION.cff` — provisional software citation metadata (no invented DOI).
- `PUBLIC_RELEASE_CHECKLIST.md` — release steps and unresolved license decision.

The exact input ZIP has SHA-256 `d2cde0943b2a55e02bc0e5613c7274724a61104c48ea6c6ef798d66eeee266c1`. The `supplement/` tree is a literal extraction of the input archive, preserving the earlier release's internal README and its as-of-date status language. **This top-level README is the current description.** No theorem statement, proof, or manuscript source was modified as part of the repository packaging.

## Reproduce the exact certificates

Python 3 and SymPy **1.14.0** are required. On Linux, macOS or WSL:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r supplement/requirements.txt
python run_checks.py
```

The runner first verifies all original `SHA256SUMS.txt` entries, then executes both checkers with Python assertions enabled and compares the parsed JSON outputs to the saved reference files. It writes output only into the ignored `reproduced/` directory.

Run the underlying scripts individually if desired:

```bash
cd supplement
python verify_publication.py > ../reproduced/publication.json
python verify_historical_counts.py > ../reproduced/historical.json
```

These exact computations are **supporting certificates**, not a formal proof assistant, a substitute for the article's geometric arguments, or an independent human mathematical review. The historical point counts are authenticated input data; they are not freshly enumerated by the scripts. The main article's theorem assessments—including substantive evaluation of its exterior–Brauer theorem—belong to journal peer review.

## Archival citation

For a stable scholarly citation, publish a GitHub release and archive that version in **Zenodo**, which provides a DOI. Use the version-specific DOI in the manuscript's Code Availability / Data Availability statements. No DOI should be cited until it exists.

## Reuse and license

Python software: MIT License (`LICENSE`).

Original documentation and research data: Creative Commons Attribution 4.0 International (`LICENSE_CONTENT.md`), subject to the stated rights and provenance restrictions.

## Scope and provenance

This repository contains only the reproducibility materials supplied for the NR130 journal submission, not the full historical KUMMER research archive. It does not include the manuscript itself, which is kept in the author's separate publication working directory. Author retains responsibility for accuracy and publication decisions.
