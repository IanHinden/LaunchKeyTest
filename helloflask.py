from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstra = Bootstrap(app)
app.config['SECRET_KEY'] = "Welcometolaunchkey"
app.debug = True

class LoginForm(FlaskForm):
	username = StringField("username", validators=[InputRequired(), Length(min=4, max=15)])
	password = PasswordField("password", validators=[InputRequired(), Length(min=8)])

@app.route("/")
def index():
	form = LoginForm()
	
	return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run()