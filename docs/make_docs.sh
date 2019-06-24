echo "Installing lingcorpora"
pip3 install .. --user
echo "Successfully installed lingcorpora."
echo "Building HTML..."
sphinx-build -b html ./source ./html
echo "Docs for lingcorpora are built."
