# vape-sensor-inventory

## Setup
> Dev setup     

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

1. Bootstrap Flask (in progress)
2. Database provision          

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
