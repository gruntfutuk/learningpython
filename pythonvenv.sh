#!/bin/bash
# create a command to create python3 virtual environment
python3 -m venv $1
source venv/bin/activate
cd venv
