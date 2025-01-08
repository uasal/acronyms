# Simply for compiling compile-test.tex to see if it has errors. No error catching at the moment / using latex warnings for troubleshooting if there are problems with edits.

# Setup gitinfo
sed -i -e 's/\r$//' gitinfo2-hook.sh
bash gitinfo2-hook.sh

# Using -shell-escape in case this repo becomes a latex documentation template and minted is used.
xelatex -shell-escape compile-test.tex
xelatex -shell-escape compile-test.tex

