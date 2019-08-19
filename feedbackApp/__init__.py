import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5809@localhost/feedbackAPP'
else:
	pass


##################DataBase Setup#####################



# Settings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# Variables
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#######################################################


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)


from feedbackApp.core.views import core
from feedbackApp.error_pages.handlers import error_pages



app.register_blueprint(core)
app.register_blueprint(error_pages)
