import connexion
import repositories.db as DB
from healthcheck import HealthCheck
from flask_cors import CORS
from controllers import bearing_info_controller as controllers

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml', validate_responses=True)

# Api health check
app_health = HealthCheck()
# Mongo connection
DB.connect_db()

# Api health check
app.add_url_rule("/vapehealthcheck", "vapehealthcheck", view_func=lambda: app_health.run())

# enable CORS
cors = CORS(app.app)

if __name__ == '__main__':
    app.run(port=8822)

