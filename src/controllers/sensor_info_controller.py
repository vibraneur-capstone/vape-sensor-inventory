from mongoFacade import sensor_info as facade
from mapper.bearing_detail_mapper import to_bearing_detail
from mapper.sensor_summary_mapper import to_sensor_detail

HEADER = {"Access-Control-Allow-Origin": "*"}

def post_new_sensor(body):
    sensor_status = body['sensor_status']
    tags = body['tags']
    install_time = None
    if ('install_time' in body):
        install_time = body['install_time']
    sensor = facade.create_new_sensor(tags, sensor_status, install_time)
    sensor = to_sensor_detail(sensor)
    return sensor, 200, HEADER 

    
