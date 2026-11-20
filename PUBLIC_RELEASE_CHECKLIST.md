# Public GitHub + Zenodo release checklist

**Proposed repository name:** `kummer-heron-quartics-reproducibility`

1. **Choose the license explicitly before publishing.** Recommended split if you agree: MIT for `.py` source; CC BY 4.0 for documentation and archived numerical data. Alternatively consider BSD-3-Clause for code. Do not apply one of these licenses without the author's approval or invent a license for the archived predecessor files. If rights to some retained files are uncertain, preserve them without an explicit reuse license and indicate that scope.
2. Run `python run_checks.py` and review `README.md`, the included original ESM zip, and every file for material you do not wish to make public.
3. Create a **public** GitHub repository named `kummer-heron-quartics-reproducibility` under your chosen account. Upload or commit the contents of this folder (do not commit your `.venv`).
4. In Zenodo's GitHub integration, authorize GitHub and enable archiving for **this repository before cutting the release**. Official guide: https://help.zenodo.org/docs/github/enable-repository/
5. Create an annotated `v1.0.0` release on GitHub. Zenodo will archive the release and create a DOI. Verify that its record includes the correct author, title, keywords, license and files.
6. Copy the **actual** GitHub URL and **actual** version-specific Zenodo DOI into the manuscript's Code Availability and Data Availability text. Do not invent either.
7. Keep the original journal supplement ZIP (SHA-256 `d2cde0943b2a55e02bc0e5613c7274724a61104c48ea6c6ef798d66eeee266c1`) immutable. If you revise public source code after this release, make a **new tagged release**, never silently overwrite the archived version.
8. Upload the journal's `ESM_1.zip` if Editorial Manager asks for supplementary files; use the public repository/Zenodo DOI as an additional availability reference. Ask the journal whether duplicate ESM upload is necessary if it is already accessible by DOI.

## Example local GitHub commands (requires your credentials and GitHub CLI)

```bash
cd ~/research/triangle-kummer-publication/supplement-repository
python run_checks.py
git init
git branch -M main
git add .
git commit -m "Initial NR130 reproducibility supplement"
gh auth login
gh repo create kummer-heron-quartics-reproducibility --public --source=. --remote=origin --push
# In Zenodo: enable GitHub repository BEFORE creating the release.
gh release create v1.0.0 --title "v1.0.0 — NR130 exact certificates" --notes "Reproducibility supplement for the K3 surface manuscript"
```

**No GitHub repository, release, Zenodo deposit, DOI, or manuscript amendment was created by preparing this local package.**
