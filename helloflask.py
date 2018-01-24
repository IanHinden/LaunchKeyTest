from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.debug = True
app.config['SECRET_KEY'] = "Welcometolaunchkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/ianhinden/Documents/Programming/LaunchKeyTest/LaunchKeyTest/database.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(), unique=True)
	email = db.Column(db.String(), unique=True)
	password = db.Column(db.String())
	phone = db.Column(db.String(), unique=True)


class LoginForm(FlaskForm):
	username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField("password", validators=[InputRequired(), Length(min=8)])
	submit = SubmitField('Sign In')

@app.route("/", methods=['GET', 'POST'])
def index():
	form = LoginForm()
	
	return render_template("index.html", form=form)
	
@app.route("/welcome.html", methods=["POST"])
def welcome():

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				return '<h1>' + 'Welcome, ' + form.username.data + '.' + '</h1>'
		return '<h1>Invalid username or password</h1>'
	
if __name__ == "__main__":
    app.run()