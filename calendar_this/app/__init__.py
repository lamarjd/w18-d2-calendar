from app import routes
from flask import (Flask, render_template)
import os

# creates the Flask app, gets the secret key from the environment, and registers the Blueprint. 


# In the article, you were encouraged to create a Config class in a config module so that you could use app.config.from_object. This is an alternate way of doing it, the app.config.update method takes a dictionary and uses it in much the same way that app.config.from_object iterates over the attributes of the object and sets the configuration from that.
app = Flask(__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)