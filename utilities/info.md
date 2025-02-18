[![Markdown Acronym Workflow](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml/badge.svg)](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml)

# UASAL / Acronyms
For storing the latest versions of acronyms for other repos to pull from. The [`combined_acronyms.tex`](combined_acronyms.tex) file was generating by using non-duplicate values from original .tex files found in other repos and on Overleaf. These can be viewed in the [archives](archives/) directory. The purpose of having one acronym.tex file instead of multiple is to limit issues with compiling latex documentation if there are duplicate listings. A rough script for generating a markdown file from the combined .tex acronyms file provided as well. Use the `glossaries.tex` file for adding additional terms that are not acronyms to the glossary for latex to use.

## Editing Information
- Apply updates to the [`combined_acronyms.tex`](combined_acronyms.tex) file. 
  - Use format: `\newacronym{label}{ABBREVIATION}{long-form of the term}`
  - **Verify** there is no other acronym in the file that has the same label *(CI check for this as well)*
- Update `Modified` section in [`combined_acronyms.tex`](combined_acronyms.tex) with the date you edited the file.
  - Add the date last modified (not automatic presently) 
- GitHub workflow will update this `README.md` and include the markdown conversion to display below and add a new [`combined-acronyms.md`](combined-acronyms.md) file with the adjustments.
  - Update `README.md` by editing the [`info.md`](utilities/info.md) in the utilities directory (for edit to this _top_ half of the `README.md`)
  - This format can be changed to a markdown table if of use in the future.
- A latex pdf is generated as well with both acronyms **and** glossary terms which can be found here: [combined-test.pdf](combined-test.pdf)
  - **NOTE:** This was a test feature / an output of the CI latex test compiling method mainly

**Results of the last latex to markdown conversion run shown below:**

---------------------------------
