#!/usr/bin/env bash

# Run the application in debug mode


pip install --editable .
test -d debug/output || mkdir -p debug/output

trend-analysis
