from mongoFacade.models import AlertStatus


def to_bearing_count(bearings):
    return {
        "total": len(bearings),
        "ok": count_by_bearing_status(AlertStatus.OK, bearings),
        "insufficientData": count_by_bearing_status(AlertStatus.INSUFFICIENT_DATA, bearings),
        "alarm": count_by_bearing_status(AlertStatus.ALARM, bearings)
    }


def count_by_bearing_status(status, bearing_list):
    match = filter(lambda bearing: bearing.alert_status == status, bearing_list)
    return sum(1 for m in match)
