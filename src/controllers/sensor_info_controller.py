from mapper import swagger_mapper as mapper
from mongoFacade import sensor_info as facade

HEADER = {"Access-Control-Allow-Origin": "*"}


def get_sensors_summary(org_name, status):
    sensors_query_set = facade.get_sensors_by_org_name_and_status(org_name, status)
    sensors_summary = mapper.to_sensor_summary_list(sensors_query_set)
    return sensors_summary, 200, HEADER


def get_sensors_count(org_name):
    sensors = facade.get_all_sensors_by_org_name(org_name)
    sensors_count = mapper.to_sensor_count(sensors)
    return sensors_count, 200, HEADER


def get_sensor_detail(id):
    sensor_detail = facade.get_sensor_by_id(id)
    sensor_detail = mapper.to_sensor_detail(sensor_detail)
    return sensor_detail, 200, HEADER


def patch_sensor_tags(id, tags):
    sensor = facade.update_sensor_tags(id, tags)
    sensor = mapper.to_sensor_detail(sensor)
    return sensor, 200, HEADER
