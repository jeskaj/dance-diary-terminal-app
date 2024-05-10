#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo 'ERROR: Dance Diary was created using Python 3.10.12 and you do not have Python3 installed.
       To install Python3, please go to: https://www.python.org/downloads/ and install version 3.10.12 or higher.' >&2
    exit 1
fi

if ! [[ -x "$(command -v pip3)" ]]
    then
    echo 'ERROR: pip3 is not installed.
        To install pip3, please go to: https://pypi.org/project/pip/' >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py