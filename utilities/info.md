[![Markdown Acronym Workflow](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml/badge.svg)](https://github.com/sfrinaldi/acronyms-test/actions/workflows/md-workflow.yml)

# UASAL / Acronyms
For storing the latest versions of acronyms for other repos to pull from. The [`combined_acronyms.tex`](combined_acronyms.tex) file was generating by using non-duplicate values from original .tex files found in other repos and on Overleaf. These can be viewed in the [archives](archives/) directory. The purpose of having one acronym.tex file instead of multiple is to limit issues with compiling latex documentation if there are duplicate listings. A rough script for generating a markdown file from the combined .tex acronyms file provided as well.

## Editing Information
- Apply updates to the [`combined_acronyms.tex`](combined_acronyms.tex) file. 
- Update `Modified` section in [`combined_acronyms.tex`](combined_acronyms.tex) with the date you edited the file.
- **VERIFY** added acronyms are not already within the dictionary as this will cause issues in latex generating repositories that use this repo for acronym pulling.
  - Eventually, a check can be added to this repo for doing automatically. 
- GitHub workflow will update this README.md files' markdown conversion run display and add a new [`combined-acronyms.md`](combined-acronyms.md) file with the adjustments.
  - This format can be changed to a markdown table if of use in the future.

**Results of the last latex to markdown conversion run shown below:**

---------------------------------
