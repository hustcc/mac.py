#!/bin/bash

python test/test_unitest.py

flake8 --format=pylint --max-line-length=120 --ignore=F403 --builtins=_ \
$(find src/macpy/ -name "*.py" -print)
