from flask import Flask
from config import Config, Configdb
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)
app.config.from_object(Configdb)
db = SQLAlchemy(app)
