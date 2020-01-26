import logging
from repositories import models 
import json
from bson import json_util


def get_all_sensors_org(org_name, status):
    logging.info("HTTP request received with org_name: %s".format(org_name))
    sensors = []
    if (status == "ALL"):
        sensors = models.Sensor.objects.filter(organization__organization_name = org_name)
    elif(status == "ONLINE"):
        sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(sensor_status = models.SensorStatus.ONLINE)
    elif(status == "OFFLINE"):
        sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(sensor_status = models.SensorStatus.OFFLINE)
    elif(status == "DECOMMISSIONED"):
        sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(sensor_status = models.SensorStatus.DECOMMISSIONED)
    return json.loads(sensors.to_json())
  
def get_all_sensors_machine(org_name, machine_name):
    logging.info("HTTP request received with org_name: %s machine_name: %s".format(org_name, machine_name))
    sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(machine__machine_name = machine_name)
    return json.loads(sensors.to_json())

def get_sensor_detail(org_name, machine_name, sensor_id):
    logging.info("HTTP request received with org_name: %s machine_name: %s id: %s".format(org_name, machine_name, sensor_id))
    sensors = models.Sensor.objects.filter(organization__organization_name = org_name).filter(machine__machine_name = machine_name)
    sensors = models.Sensor.objects.get(id = sensor_id)
    return json.loads(sensors.to_json())
  
 
