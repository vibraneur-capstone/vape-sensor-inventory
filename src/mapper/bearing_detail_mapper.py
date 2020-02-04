from mapper.sensor_summary_mapper import to_sensor_list
from mapper.machine_summary_mapper import to_machine_summary


def to_bearing_detail(bearing):
    return {
        "id": str(bearing.id),
        "status": bearing.alert_status,
        "tags": bearing.bearing_tags,
        "sensorsId": bearing.sensors_id_list,
        "sensors": to_sensor_list(bearing.sensors_id_list),
        "machineInfo": to_machine_summary(bearing.machine)
    }
