from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

class addCafeForm(FlaskForm):
    cafe_name = StringField(label="Add Cafe Name",validators=[DataRequired()])
    location = StringField(label="Add Location", validators=[URL()])
    opening = StringField(label="Add Opening Time")
    closing = StringField(label="Add Closing Time")
    rating = SelectField(label="Coffee Rating", choices = ["☕", "☕☕","☕☕☕","☕☕☕☕","☕☕☕☕☕"])
    wifi_strength = SelectField(label="Wifi Strength", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"])
    socket_availability = SelectField(label="Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"])
    submit = SubmitField(label="Add Cafe")

# ☕☕☕☕️,💪💪,🔌🔌🔌

app = Flask("__name__")
app.secret_key = ""
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafe():
    with open('cafe-data.csv', newline='', encoding='utf-8')as file:
        csvFile = csv.reader(file, delimiter=",")
        rows = []
        for lines in csvFile:
            rows.append(lines)
    return render_template("cafe.html", rows = rows)



@app.route("/add", methods = ["GET", "POST"])
def add():
    form = addCafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding="utf-8") as f:
            f.write(f"\n{form.cafe_name.data},"
                        f"{form.location.data},"
                        f"{form.opening.data},"
                        f"{form.closing.data},"
                        f"{form.rating.data},"
                        f"{form.wifi_strength.data},"
                        f"{form.socket_availability.data}")
        return redirect(url_for("cafe"))
    return render_template("add.html", form = form)



if __name__ == "__main__":
    app.run(debug=True)