#!/bin/bash

python test_unitest.py

flake8 --format=pylint --max-line-length=120 --builtins=_ \
$(find src/macpy/ -name "*.py" -print)