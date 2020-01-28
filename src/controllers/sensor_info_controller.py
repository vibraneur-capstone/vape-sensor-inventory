import logging
from repositories import models 
import json
from bson import json_util


def get_all_sensors(org_name, status):
    logging.info("HTTP request received with org_name: %s".format(org_name))
    sensors = []
    if (status == "ALL"):
        sensors = models.Sensor.objects.filter(organization__organization_name = org_name).values_list('sensor_id','sensor_status')
    else:
        status = get_status(status)
        sensors = query_func_org(org_name, status) 
    return json.loads(sensors.to_json())
  
def get_all_sensors_machine(org_name, machine_name):
    logging.info("HTTP request received with org_name: %s machine_name: %s".format(org_name, machine_name))
    sensors = query_func_machine(org_name,machine_name)
    return json.loads(sensors.to_json())

def get_sensor_detail(org_name, machine_name, sensor_id):
    logging.info("HTTP request received with org_name: %s machine_name: %s id: %s".format(org_name, machine_name, sensor_id))
    sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(machine__machine_name = machine_name)
    sensors = models.Sensor.objects.get(id = sensor_id)
    return json.loads(sensors.to_json())

######Helper functions to define query 
def query_func_machine(org_name, machine_name):
    sensors = sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(machine__machine_name = machine_name)
    return sensors.values_list('sensor_id','sensor_status')

def query_func_org(org_name, status):
    sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(sensor_status = status)
    return sensors.values_list('sensor_id','sensor_status')

def get_status(status):
    if(status == "ONLINE"):
        status = models.SensorStatus.ONLINE
    elif(status == "OFFLINE"):
        sensors = models.SensorStatus.OFFLINE
    elif(status == "DECOMMISSIONED"):
        sensors = models.SensorStatus.DECOMMISSIONED
    return status
