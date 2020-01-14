import connexion
import repositories.db as DB
import repositories.models as models
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')

#test to insert data to the data base, meant to be removed later
@app.route("/test")
def test():
    org = models.Organization(organization_name = "Husky",
    organization_city = "St. Johns")
    org.save()
    return "created a doc using mongoengine"
if __name__ == '__main__':
    app.run(port=8822)