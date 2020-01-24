import logging
from repositories import models 

def get_all_sensors_org(org_name):
    logging.info("HTTP request received with org_name: %s machine_name: %s status: %s".format(org_name))
    # TODO return dummy response
    return {"org_name": "MUN",  "status": 2}

def get_all_sensors_machine(org_name, machine_name):
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s status: %s".format(org_name, machine_name))
    # TODO return dummy response
    return {"org_name": org_name, "machine_name": machine_name}

def get_sensor_detail(org_name, machine_name, sensor_id):
    org_name = "MUN"
    machine_name = "Alpha"
    status = "Online"
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s id: %s".format(org_name, machine_name, sensor_id))
    # TODO return dummy response
    return {"org_name": org_name, "machine_name": machine_name, "id": sensor_id}

def get_online_sensors(org_name):
    return "Sensors online"

def get_offline_sensors(org_name):
    return "Sensors offline"

def get_discontinued_sensors(org_name):
    return "Sensors discontinued"
