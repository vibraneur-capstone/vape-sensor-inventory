#!/bin/bash

venv_name="venv"

echo "Init virtual environment start"

sleep 1

rm -rf $venv_name

python3 -m venv $venv_name

source $venv_name/bin/activate

printf "\nInstalling dependency \n"
sleep 1

pip3 install -r requirements.txt

printf "\nFinished... \n"

deactivate