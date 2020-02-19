from flask import Flask 
from config import Config #This imports the Config class from the config.py file
from flask_mongoengine import MongoEngine
# from flask_restplus import Api 

# api = Api()

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app) #This initialize the mongoengine database
# api.init_app(app)# Initializes the postman api
from routes import * # THis import all the routes files

if __name__ == "__main__":
    app.run(debug = True)