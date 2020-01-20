import connexion
import repositories.db as DB
import repositories.models as models
from healthcheck import HealthCheck

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')
app_health = HealthCheck()
DB.connect_db()

# TODO: override app_health to include mongoDB connection test
app.add_url_rule("/vapehealthcheck", "vapehealthcheck", view_func=lambda: app_health.run())


# test to insert data to the data base, meant to be removed later
# TODO: remove this... and implement unit test
@app.route("/test")
def test():
    org = models.Organization(organization_name="Husky",
                              organization_address="St. Johns")
    sensor = models.Sensor(sensor_name="test name",
                           sensor_status=models.SensorStatus.DECOMMISSIONED,
                           organization=org)
    sensor.save()
    return sensor.to_json()


if __name__ == '__main__':
    app.run(port=8822)
