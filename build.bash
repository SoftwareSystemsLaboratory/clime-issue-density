#!/bin/bash

rm -r dist
pip uninstall clime_issue_density -y
python -m build
pip install dist/clime_*

echo
echo "Done building"
