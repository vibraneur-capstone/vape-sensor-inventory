#!/bin/bash

dist_name="sensor-inventory-dist.zip"
package_path="package"

mkdir $package_path

python3 -m pip install -r requirements.txt --target $package_path

python3 -m pip install connexion[swagger-ui] --target $package_path

cp -a ./src/* $package_path

cd $package_path || exit

zip -r9 ${OLDPWD}/$dist_name .

cd ${OLDPWD} || exit

printf "\nCleaning up \n"
rm -rf $package_path

printf "\nFinished Building \n"
