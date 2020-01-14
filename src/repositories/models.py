from mongoengine import *

class Organization(Document):
    organization_name = StringField(required=True, max_length=50)
    organization_city = StringField(required=False, max_length=50)
    total_sensor_number = IntField(required=True, default=0)

class Machine(Document):
    name = StringField(required=True)
    organization_id = ReferenceField(Organization, required=False)

class Sensor(Document):
    sensor_name = StringField(required=True)
    organization_id = ReferenceField(Organization, required=True)
    machine_id = ReferenceField(Machine, required=True)
    sensor_install_time = DateField(required=False)
    sensor_status = StringField(required=True, max_length=50)