[![Markdown Acronym Workflow](https://github.com/sfrinaldi/acronyms-fork/actions/workflows/ci.yml/badge.svg)](https://github.com/sfrinaldi/acronyms-fork/actions/workflows/ci.yml)

> [!Note]
> The following information was generated automatically by pulling from [info.md](utilities/info.md) and [uasal-acronyms.tex](uasal-acronyms.tex) to create this updated `README.md` file.

# UASAL / Acronyms
For storing the latest versions of acronyms for other repos to pull from. The [`uasal-acronyms.tex`](uasal-acronyms.tex) file was generating by using non-duplicate values from original .tex files found in other repos and on Overleaf. These can be viewed in the [archives](archives/) directory. The purpose of having one acronym.tex file instead of multiple is to limit issues with compiling latex documentation if there are duplicate listings. A rough script for generating a markdown file from the combined .tex acronyms file provided as well. Use the `glossaries.tex` file for adding additional terms that are not acronyms to the glossary for latex to use.

## Adding New Acronyms
> [!Warning]
> UASAL Automatic Latex Documentation Repositories may be using the `uasal-acronyms.tex` from this repository for their workflows. <br>
> 
> Do **NOT** re-name the `uasal-acronyms.tex` unless prepared to edit other repositories thar are looking for this specific file within their workflows.

1. Create a new branch _or_ update using the `develop` branch
2. Create a new Pull Request to update `main` as draft
3. Edit [`uasal-acronyms.tex`](uasal-acronyms.tex) 
     - **Format:** `\newacronym{label}{ABBREVIATION}{long-form of the term}`
     - **Verify** there is no other acronym in the file that has the same label *(CI check for this as well)*
4. Update `Modified` section in [`uasal-acronyms.tex`](uasal-acronyms.tex) with the new date last modified value
     - *Not automatic presently for markdown output*
5. Change Pull Request from draft to ready for review
6. Assign Reviewer (ex. sfrinaldi, douglase)
  
> [!Note]
> A latex pdf is generated as well with both acronyms **and** glossary terms which can be found here: [compiled-acronyms.pdf](https://github.com/sfrinaldi/acronyms-fork/tree/compiled/compiled-acronyms.pdf)


## CI Output Documentation
This repository outputs the results of the workflow for this repo to the [compiled](https://github.com/sfrinaldi/acronyms-fork/tree/compiled) branch. This includes the `compiled-acronyms.pdf` which has both acronyms and related information such as glossaries and citations. An automatic version of the markdown file that is created is provided both below for quick reference and on the compiled branch (both generated and updated by the same workflow).

> [!Note]
> The following information was generated automatically by pulling information from [compiled-acronyms.tex](compiled-acronyms.tex) that was converted to markdown using a test [script](utilities/latex_acronyms-to-markdown.py) that was added to this `README.md`.

---------------------------------
