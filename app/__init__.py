# Import flask and template operators
from flask import Flask

# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)
  # When we run tests, we pass new value for config with a dict.
  if type(config_name) is dict:
    app.config.update(config_name)
  else:
    app.config.from_object(app_config[config_name])
  from app.controllers import module_home
  app.register_blueprint(module_home)
  db.init_app(app)
  # As we declare db in global, we need to push context.
  app.app_context().push()
  db.create_all()
  return app