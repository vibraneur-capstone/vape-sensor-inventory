def to_machine_summary(machine):
    return {
        "name": machine.machine_name,
        "location": machine.location,
        "alertStatus": machine.alert_status
    }