from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from launchkey.factories import ServiceFactory, DirectoryFactory, OrganizationFactory

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.debug = True
app.config['SECRET_KEY'] = "Welcometolaunchkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/ianhinden/Documents/Programming/LaunchKeyTest/LaunchKeyTest/database.db'
db = SQLAlchemy(app)

organization_id = "9eb44784-ffb6-11e7-beac-32c85991b6e3"
organization_private_key = open('organization_private_key.key').read()
directory_id = "8d8bc0e2-015d-11e8-9daa-16cd5ddd3780"
service_id = "df4d2d1a-ffb6-11e7-a5f3-4697f50c1dd9"
service_private_key = open('service_private_key.key').read()

service_factory = ServiceFactory(service_id, service_private_key)
organization_factory = OrganizationFactory(organization_id, organization_private_key)
directory_client = organization_factory.make_directory_client(directory_id)
service_client = organization_factory.make_service_client(service_id)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(), unique=True)
	email = db.Column(db.String(), unique=True)
	password = db.Column(db.String())
	phone = db.Column(db.String(), unique=True)


class LoginForm(FlaskForm):
	username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
	#password = PasswordField("password", validators=[InputRequired(), Length(min=8)])
	submit = SubmitField('Sign In')

@app.route("/", methods=['GET', 'POST'])
def index():
	form = LoginForm()
	
	return render_template("index.html", form=form)
	
@app.route("/welcome.html", methods=["POST"])
def welcome():

	form = LoginForm()

	if form.validate_on_submit():
		user = "IanHinden"#User.query.filter_by(username=form.username.data).first()
		#if user:
			#if user.password == form.password.data:
				#return '<h1>' + 'Welcome, ' + form.username.data + '.' + '</h1>'
		link_data = directory_client.link_device(user)
		linking_code = link_data.code
		qr_url = link_data.qrcode
		return "Scan the QR code at this URL to link your device: " + qr_url
		#return '<h1>Invalid username or password</h1>'
	
if __name__ == "__main__":
    app.run()