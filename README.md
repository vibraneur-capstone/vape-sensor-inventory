# vape-sensor-inventory

## About this micro service
This micro-service is powered by *Flask* with *connexion* which auto handles all HTTP request mapping       
For details refer to `swagger.yaml`

## Release Note (Feb 2, 2020)
1. Refactored code structure to follow best practices including the use of `facade`, and `DTO` mapper, to improve code readability and maintainability.   
2. Previous Violations to Swagger contract have all been resolved.
3. Enabled `response validation` in Flask App to ensure developer maintain the integrity of swagger
4. TODO items: refer to [TODO section](#todo-fed-2-2019)

## Setup
> Install `pip`     
> Make sure to have python3     
> that's it

## Running on Local
>A script is provided to help with dev setup and running     
>
>From project root directory, run `./scripts/init_venv.sh` will create a virtual env and install all dependencies  
>      
>After virtual env is set up, run `./scripts/run_server.sh` will boot up the server on localhost:8822       

## API Endpoints

### Note: API testing should strictly be based on swagger file, NOT any source of documentation     

### Use swagger file to examine Endpoint structure [click here for swagger editor](https://editor.swagger.io/)
> Note: To try it out in Dev environment using swagger editor, update the `host` to `host: sensor.vibraneur.com` and `schemes` to `HTTPS`. To try it out in Local environemnt using editor, udpate the `host` to your `loopback address` and `schemes` to `HTTP`, NOT `HTTPS`.
> Dev envirinment will NOT redirect HTTP call to HTTPS. It is developer's repsponsibility to ensure usage of HTTPS calls

## TODO (Fed 2, 2019)

1. ~~Bootstrap Flask (in progress) (Done)~~
2. ~~Database provision (done)~~         
3. ~~Team meeting~~
4. Unit Test (Long overdue)...

## Swagger

> Copy and paste swagger file to online editor to view API structure [here](https://editor.swagger.io/)

## Swagger file validation

> install `swagger-cli` using `npm`: run `npm i -g swagger-cli`         
> validate file by running `swagger-cli validate ./swagger/swagger.yaml`
> Online editor also provides validation [here](https://editor.swagger.io/)

## API Requirements:
Database implemented in no-sql in dynomoDB or mongoDB
- Will probably have to listen to kafka pipeline
- Heartbeat to indicate sensor is healthy
- Sensors and bearings in the same database

1. Ability to query a list of installed sensors 
2. Ability to query the status of each sensor
3. Ability to query information about a sensor
4. Query the total number of sensors
5. Ability to add a new sensor
6. Ability to remove a sensor
7. Ability to check the health of a sensor 
