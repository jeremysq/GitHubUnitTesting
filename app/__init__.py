from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app,origins=['*'])

from app import views