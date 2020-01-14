import connexion
import repositories.db as DB
import repositories.models as models

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')
DB.connect_db()


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
