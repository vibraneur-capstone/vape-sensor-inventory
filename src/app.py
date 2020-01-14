import connexion
import repositories.db as DB
import repositories.models as models
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')

#test to insert data to the data base, meant to be removed later
@app.route("/test")
def test():
    user = models.User(email="connect@derrickmwiti.com", first_name="Derrick", last_name="Mwiti")
    user.save()
    return "created a sensor--mongoengine"
if __name__ == '__main__':
    app.run(port=8822)