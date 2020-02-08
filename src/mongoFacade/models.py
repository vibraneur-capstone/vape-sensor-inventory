from mongoengine import *
from enum import Enum


class SensorStatus(str, Enum):
    ONLINE = "ONLINE"
    DECOMMISSIONED = "DECOMMISSIONED"
    OFFLINE = "OFFLINE"
    ALL = "ALL"


class AlertStatus(str, Enum):
    ALARM = "ALARM"
    OK = "OK"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    DISCONTINUED = "DISCONTINUED"
    ALL = "ALL"


class Organization(EmbeddedDocument):
    organization_name = StringField(required=True, max_length=50)
    organization_address = StringField(required=False, max_length=50)


class Machine(EmbeddedDocument):
    machine_name = StringField(required=True, default="")
    organization_name = StringField(required=True, max_length=50, default="")
    location = StringField(required=False, default="")
    alert_status = StringField(required=True, max_length=50, default=AlertStatus.INSUFFICIENT_DATA)


class Sensor(Document):
    sensor_install_time = DateField(required=False)
    sensor_status = StringField(required=True, max_length=50)
    sensor_tags = DictField(required=True, default={})


class Bearing(Document):
    machine = EmbeddedDocumentField(Machine, required=False)
    organization = EmbeddedDocumentField(Organization, required=False)
    bearing_tags = DictField(required=True, default={})
    alert_status = StringField(required=True, max_length=50, default=AlertStatus.INSUFFICIENT_DATA)
    sensors_id_list = ListField(required=True, default=[])


