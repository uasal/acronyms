# For converting uasal-acronyms.tex file into an easy-to-read markdown file
# Requires uasal-acronym.tex file to have appropriate line prefixes to work correctly.
# Refer to the comment section within the uasal-acronym.tex file for details.
# CI checker for uasal-acronyms.tex has been implemented for verifying duplicate entries where this will result in an error in
# Latex Generating Repositories that pull from this repo and/or use it as a submodule.

# Created- 17-MAY-24
# Author- SFR
# Last Modified- 28-MAY-25

# Package Imports
import os


# For replacing parts of the line with different values to convert to markdown
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


# Variables
output_File = open("uasal-acronyms.md", "a+")
input_File = open("uasal-acronyms.tex", "r")
info_File = open("utilities/info.md", "r")
readme_File = open("README.md", "w")
replacements = {"%%+": "##", "%+": "#", "%%": "-", "%": "##", "\\newacronym{": "- ", "$\\textit{": "*", "\\newacronym[": "- ", "plural=": "Plural= ", " firstPlural=": "", "$^{": "^", "{\\gls{": "-> Lower-Case: ","\\gls{": "-> Lower-Case= ", "/\\gls{": "-> Lower-Case: ", "$\\approx$": "~", "description=": "Description= ", "$\\&$": "&", "]{": " -> ", "} ":" -> ", "[p": "P", "$": "", "}{": " -> ", "}": "", "\\epsilon": "$\\epsilon$"}
current_DIR = os.getcwd()
# Will need to change this depending on where the acronyms will live in repo
# acronym_DIR = os.path.join(current_DIR, '/resources/acronyms.tex')

# Readme update (first part)
for line in info_File:
    readme_File.write(line)
info_File.close()

# Markdown Writing
for line in input_File:
    adjusted_line = replace_all(line, replacements)
    if line.startswith("%-"):
        print("skipping line")
    else:
        if line.startswith("% "):
            adjusted_line = "---------------------------------\n\n" + adjusted_line + "\n"
            output_File.write(adjusted_line)

            #print("Writing adjusted lines and adding spacer...")
        else:
            output_File.write(adjusted_line)
            #print("Writing adjusted lines...")
        readme_File.write(adjusted_line)

# Closing out files
input_File.close()
readme_File.close()
output_File.close()

print("Combined-acronyms.md file created. README.md updated.")
