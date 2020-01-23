import logging


def get_all_sensors(org_name, machine_name, status):
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s status: %s".format(org_name, machine_name, status))
    # TODO return dummy response
    response = {
        "sensorList": [
            {
                "id": 'b14567',
                "status": 'ONLINE'
            },
            {
                "id": 'b14568',
                "status": 'OFFLINE'
            },
            {
                "id": 'b14569',
                "status": 'DECOMMISSIONED'
            },
            {
                "id": 'b14570',
                "status": 'ONLINE'
            },
            {
                "id": 'b14571',
                "status": 'ONLINE'
            },
        ],
        "count": 5
    }

    return response

def get_sensor_detail(org_name, machine_name, sensor_id):
    # TODO implement actual logic... this is just for testing
    logging.info("HTTP request received with org_name: %s machine_name: %s id: %s".format(org_name, machine_name, sensor_id))
    # TODO return dummy response
    return {"org_name": org_name, "machine_name": machine_name, "id": sensor_id, "status": 'ONLINE'}
