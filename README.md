# vape-sensor-inventory

## About this micro service
This micro-service is powered by *Flask* with *connexion* which auto handles all HTTP request mapping       
For details refer to `swagger.yaml`

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
*Replace value in { } with real value*

### Get Swagger UI in Browser
> type in browser `http://localhost:8822/inventory/v1/ui`     
### Query detail of a sensor
> GET: `http://localhost:8822/inventory/v1/{organization_name}/machine/{machine_name}/sensors/{sensor_id}` 
### Query a list of sensors (By default return all status)     
> GET: `http://localhost:8822/inventory/v1/{organization_name/machine/{machine_name}/sensors?status={ONLINE}`       

## Update (Dec 5th)

Swagger file created for 1-4 requirements       
```
1. Ability to query a list of installed sensors 
2. Ability to query the status of each sensor
3. Ability to query information about a sensor
4. Query the total number of sensors
```
Two endpoints, both `GET`

## TODO (Dec 5th)

1. ~~Bootstrap Flask (in progress) (Done)~~
2. Database provision (In progress)         
3. Team meeting

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
