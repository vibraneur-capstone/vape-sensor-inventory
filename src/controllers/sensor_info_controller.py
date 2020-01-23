import logging


def get_all_sensors(org_name, machine_name, status):
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s status: %s".format(org_name, machine_name, status))
    # TODO return dummy response
    return {"org_name": org_name, "machine_name": machine_name, "status": status}


def get_sensor_detail(org_name, machine_name, sensor_id):
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s id: %s".format(org_name, machine_name, sensor_id))
    # TODO return dummy response
    return {"org_name": org_name, "machine_name": machine_name, "id": sensor_id}
