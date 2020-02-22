from mongoFacade import bearing_info as facade
from mapper.bearing_detail_mapper import to_bearing_detail
from mapper.bearing_count_mapper import to_bearing_count
from mapper.bearing_summary_mapper import to_bearing_summary_list

HEADER = {"Access-Control-Allow-Origin": "*"}


def get_bearing_summary(org_name, status):
    bearings_query_set = facade.get_bearings_by_org_name_and_status(org_name, status)
    bearings_summary = to_bearing_summary_list(bearings_query_set)
    return bearings_summary, 200, HEADER


def get_bearing_count(org_name):
    bearing = facade.get_all_bearings_by_org_name(org_name)
    bearing_count = to_bearing_count(bearing)
    return bearing_count, 200, HEADER

def get_bearing_detail(id):
    bearing_detail = facade.get_bearing_by_id(id)
    bearing_detail = to_bearing_detail(bearing_detail)
    return bearing_detail, 200, HEADER

def patch_bearing_tags(id, tags):
    bearing = facade.update_bearing_tags(id, tags)
    bearing = to_bearing_detail(bearing)
    return bearing, 200, HEADER

def post_new_bearing(body):
    org_name = "Husky"
    tags = body["tags"]
    sensors_list_id = body["sensorId"]
    bearing = facade.create_new_bearing(org_name, tags, sensors_list_id)
    bearing = to_bearing_detail(bearing)
    return bearing, 200, HEADER

def attach_sensor_to_bearing(bearing_id, sensor_id):
    bearing = facade.add_sensor_id_to_bearing(bearing_id, sensor_id)
    bearing = to_bearing_detail(bearing)
    return bearing, 200, HEADER


    

