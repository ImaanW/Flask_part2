from flask import Flask
# instantiate
app = Flask(__name__)

from application import routes
