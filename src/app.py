import connexion
import repositories.db as DB
import repositories.models as models
from healthcheck import HealthCheck
from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')

# Api health check
app_health = HealthCheck()
# Mongo connection
DB.connect_db()

# Api health check
app.add_url_rule("/vapehealthcheck", "vapehealthcheck", view_func=lambda: app_health.run())

# enable CORS
cors = CORS(app.app)

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
    app.run(port=8822, debug = True)


