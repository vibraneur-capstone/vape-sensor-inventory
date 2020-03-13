from mongoFacade.bearing_info import get_sensor_by_id


def to_sensor_list(sensor_id_list):
    sensor_id_list = list(map(lambda id: to_sensor(id), sensor_id_list))
    return sensor_id_list


def to_sensor(sensor_id):
    sensor = get_sensor_by_id(sensor_id)
    if sensor is None:
        return None
    return {
        "id": str(sensor.id),
        "status": sensor.sensor_status,
        "tags": sensor.sensor_tags,
        "installTime": sensor.sensor_install_time
    }


def to_sensor_detail(sensor):
    return {
        "id": str(sensor.id),
        "sensor_status": sensor.sensor_status,
        "tags": sensor.sensor_tags,
        "installTime": sensor.sensor_install_time
    }
