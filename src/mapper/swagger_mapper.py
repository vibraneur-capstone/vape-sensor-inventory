import json
from mongoFacade.models import SensorStatus


def to_sensor_count(sensors):
    return {
        "total": len(sensors),
        "online": count_by_sensor_status(SensorStatus.ONLINE, sensors),
        "offline": count_by_sensor_status(SensorStatus.OFFLINE, sensors),
        "decommissioned": count_by_sensor_status(SensorStatus.DECOMMISSIONED, sensors)
    }


def to_sensor_summary_list(sensor_query_set):
    sensor_query_json = json.loads(sensor_query_set.to_json())
    sensor_summary_list = list(map(to_sensor_summary, sensor_query_json))
    return {
        "sensors": sensor_summary_list,
        "count": len(sensor_summary_list)
    }


def to_sensor_detail(sensor):
    sensor_json = json.loads(sensor.to_json())
    return {
        "id": sensor_json["_id"]["$oid"],
        "status": sensor_json["sensor_status"],
        "name": sensor_json["sensor_name"],
        "tags": sensor["sensor_tags"],
        "machineInfo": to_machine_summary(sensor_json["machine"])
    }


def to_machine_summary(machine):
    return {
        "name": machine["machine_name"],
        "location": machine["location"],
        "alertStatus": machine["alert_status"]
    }


def to_sensor_summary(sensor):
    return {
        "id": sensor["_id"]["$oid"],
        "status": sensor["sensor_status"],
        "tags": sensor["sensor_tags"]
    }


def count_by_sensor_status(status, sensor_list):
    match = filter(lambda sensor: sensor.sensor_status == status, sensor_list)
    return sum(1 for m in match)