
def to_bearing_summary_list(bearing_query_set):
    bearing_summary_list = list(map(to_bearing_summary, bearing_query_set))
    return {
        "bearingList": bearing_summary_list,
        "count": len(bearing_summary_list)
    }


def to_bearing_summary(bearing):
    return {
        "id": str(bearing.id),
        "status": bearing.alert_status,
        "tags": bearing.bearing_tags,
        "sensorsId": bearing.sensors_id_list
    }
