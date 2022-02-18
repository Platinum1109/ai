import os
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Platinum'

from app import views

