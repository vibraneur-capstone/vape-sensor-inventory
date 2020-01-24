from mongoengine import *
from enum import Enum


class Organization(EmbeddedDocument):
    organization_name = StringField(required=True, max_length=50)
    organization_address = StringField(required=False, max_length=50)
    total_sensor_count = IntField(required=True, default=0)
    total_machine_count = IntField(required=True, default=0)


class Machine(EmbeddedDocument):
    machine_name = StringField(required=True)
    organization_name = StringField(required=True, max_length=50)
    location = StringField(required=False)
    total_sensor_count = IntField(required=True, default=0)


class Sensor(Document):
    id = StringField(required=False)
    sensor_name = StringField(required=True)
    organization = EmbeddedDocumentField(Organization, required=False)
    machine = EmbeddedDocumentField(Machine, required=False)
    sensor_install_time = DateField(required=False)
    sensor_status = StringField(required=True, max_length=50)

class SensorStatus(str, Enum):
    ONLINE = "ONLINE"
    DECOMMISSIONED = "DECOMMISSIONED"
    OFFLINE = "OFFLINE"
