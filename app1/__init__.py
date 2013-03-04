from flask import Flask

app1 = Flask(__name__)
app1.config.from_object('config')

from app1 import views

