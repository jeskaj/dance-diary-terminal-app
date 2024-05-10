#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate

echo Hello, what is your name?

read varname

echo It\'s nice to meat you $varname