from mongoFacade.models import Bearing
from mongoFacade.models import AlertStatus
from mongoFacade.models import Sensor


def get_bearings_by_org_name_and_status(org_name, status):
    if status == AlertStatus.ALL:
        bearings = Bearing.objects(organization__organization_name=org_name)
    else:
        bearings = Bearing.objects(organization__organization_name=org_name, alert_status=status)
    return bearings


def get_bearing_by_id(id):
    return Bearing.objects.get(id=id)


def get_all_bearings_by_org_name(org_name):
    return Bearing.objects(organization__organization_name=org_name)


def update_bearing_tags(bearing_id, tags):
    bearing = get_bearing_by_id(bearing_id)
    bearing.bearing_tags.update(tags)
    bearing.save()
    return bearing


def get_sensor_by_id(id):
    return Sensor.objects.get(id=id)
