from mongoFacade.models import Bearing
from mongoFacade.models import AlertStatus
from mongoFacade.models import Sensor
from mongoFacade.models import Machine
from mongoFacade.models import Organization
from controllers.controller_config import HEADER




def get_bearings_by_org_name_and_status(org_name, status):
    if status == AlertStatus.ALL:
        bearings = Bearing.objects(organization__organization_name=org_name)
    else:
        bearings = Bearing.objects(organization__organization_name=org_name, alert_status=status)
    return bearings

def get_bearing_by_id(id):
    try:
        return Bearing.objects.get(id=id)
    except Bearing.DoesNotExist:
        return None, 400, HEADER

def get_all_bearings_by_org_name(org_name):
    try:
        return Bearing.objects(organization__organization_name=org_name)
    except Bearing.DoesNotExist:
        return None, 400, HEADER

def update_bearing_tags(bearing_id, tags):
    bearing = get_bearing_by_id(bearing_id)
    bearing.bearing_tags.update(tags)
    bearing.save()
    return bearing

def get_sensor_by_id(id):
    try:
        return Sensor.objects.get(id=id)
    except Sensor.DoesNotExist:
        return None, 400, HEADER

def add_sensor_id_to_bearing(bearing_id,sensor_id):
    bearing = get_bearing_by_id(bearing_id)
    bearing.sensors_id_list.append(sensor_id)
    bearing.save()
    return bearing

def create_new_bearing(org_name, tags, sensors_id_list):
    machine = Machine(organization_name = org_name)
    organization = Organization(organization_name = org_name)
    alert_status = AlertStatus.INSUFFICIENT_DATA
    bearing = Bearing(machine = machine, organization = organization, sensors_id_list = sensors_id_list, bearing_tags = tags, alert_status = alert_status)
    bearing.save()
    return bearing



