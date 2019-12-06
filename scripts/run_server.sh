#!/bin/bash

venv_name="venv"

source $venv_name/bin/activate

pip install connexion[swagger-ui]

python3 ./src/app.py
