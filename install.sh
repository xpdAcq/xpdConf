#!/bin/bash

conda create -n "$1" --yes
conda install -n "$1" --file requirements/build.txt --file requirements/run.txt --file requirements/test.txt -c conda-forge --yes
conda run -n "$1" pip instal -e ./ --no-deps --no-capture-output
