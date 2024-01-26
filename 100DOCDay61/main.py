"""
By the end of today, we will build a website that holds some secrets. 
Only with the right username and password can you access the page with our secrets.
"""
from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

WTF_CSRF_SECRET_KEY = 'Your Secret Key'
# This class creates a form by inheriting the Form class from wtforms
"""
WTForm are a way to create secure forms, we can create Class-based forms
and them render them in our html files however we want

"""
class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Enter a valid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(8, message="Enter atleast 8 characters")])
    submit = SubmitField(label="Log In")

app = Flask("__name__")
app.secret_key= WTF_CSRF_SECRET_KEY
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login_page():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)