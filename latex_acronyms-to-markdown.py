# For converting acronym.tex file into an easy-to-read markdown file
# Requires acronym.tex file to have appropriate line prefixes to work correctly.
# Refer to the comment section within the acronym.tex file for details.

# Created- 17-MAY-24
# Author- SFR
# Last Modified- 17-MAY-24
# Status- Draft

# Package Imports
import os


# For replacing parts of the line with different values to convert to markdown
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


# Variables
output_File = open("combined-acronyms.md", "w")
input_File = open("combined-acronyms.tex", "r")
replacements = {"%%+": "##", "%+": "#", "%%": "-", "%": "##", "\\newacronym{": "- ", "$\\textit{": "*", "\\newacronym[": "- ", "plural=": "Plural= ", " firstPlural=": "", "$^{": "^", "{\\gls{": "-> Lower-Case: ","\\gls{": "-> Lower-Case= ", "/\\gls{": "-> Lower-Case: ", "$\\approx$": "~", "description=": "Description= ", "$\\&$": "&", "]{": " -> ", "} ":" -> ", "[p": "P", "$": "", "}{": " -> ", "}": "", "\\epsilon": "$\\epsilon$"}
current_DIR = os.getcwd()
# Will need to change this depending on where the acronyms will live in repo
# acronym_DIR = os.path.join(current_DIR, '/resources/acronyms.tex')

# Markdown Writing
for line in input_File:
    adjusted_line = replace_all(line, replacements)
    if line.startswith("%-"):
        print("skipping line")
    else:
        if line.startswith("% "):
            output_File.write("---------------------------------\n\n" + adjusted_line + "\n")
            #print("Writing adjusted lines and adding spacer...")
        else:
            output_File.write(adjusted_line)
            #print("Writing adjusted lines...")

# Closing out files
output_File.close()
input_File.close()

print("Markdown Draft Created")
