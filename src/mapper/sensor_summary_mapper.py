from mongoFacade.bearing_info import get_sensor_by_id


def to_sensor_list(sensor_id_list):
    return list(map(lambda id: to_sensor(id), sensor_id_list))


def to_sensor(sensor_id):
    sensor = get_sensor_by_id(sensor_id)
    return {
        "id": str(sensor.id),
        "status": sensor.sensor_status,
        "tags": sensor.sensor_tags,
        "installTime": sensor.sensor_install_time
    }