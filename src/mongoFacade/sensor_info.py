from mongoFacade.models import Sensor
from mongoFacade.models import SensorStatus


def get_sensors_by_org_name_and_status(org_name, status):
    if status == SensorStatus.ALL:
        sensors = Sensor.objects(organization__organization_name=org_name)
    else:
        sensors = Sensor.objects(organization__organization_name=org_name, sensor_status=status)
    return sensors.values_list('sensor_id', 'sensor_status')


def get_sensor_by_id(id):
    return Sensor.objects.get(id=id)


def get_all_sensors_by_org_name(org_name):
    return Sensor.objects(organization__organization_name=org_name)