#!/bin/bash

file=${BASH_SOURCE}
dname=$(dirname ${file})

cd ${dname}
source .venv/bin/activate

python3 startNode.py
