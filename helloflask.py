from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = "Welcometolaunchkey"
app.debug = True

class LoginForm(FlaskForm):
	username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField("password", validators=[InputRequired(), Length(min=8)])
	submit = SubmitField('Sign In')

@app.route("/", methods=['GET', 'POST'])
def index():
	form = LoginForm()
	
	if form.validate_on_submit():
		return '<h1>' + 'Welcome, ' + form.username.data + '.' + '</h1>'
	
	return render_template("index.html", form=form)
	
@app.route("/welcome.html", methods=["POST"])
def welcome():
	return render_template('/welcome.html')

if __name__ == "__main__":
    app.run()