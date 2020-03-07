from mongoFacade.models import Sensor
def create_new_sensor(tags, sensor_status, install_time):
    sensor = Sensor(sensor_status = sensor_status, sensor_tags = tags, sensor_install_time = install_time)
    sensor.save()
    return sensor