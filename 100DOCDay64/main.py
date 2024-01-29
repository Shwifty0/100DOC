from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret?'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
# CREATE TABLE
class Movies(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[int] = mapped_column(String, unique=True)
    year:Mapped[int] = mapped_column(Integer)
    description:Mapped[int] = mapped_column(String)
    rating:Mapped[int] = mapped_column(Float)
    ranking:Mapped[int] = mapped_column(Integer)
    review:Mapped[int] = mapped_column(String)
    img_url:Mapped[int] = mapped_column(String)

# Edit Rating and Review FlaskForm
class UpdateForm(FlaskForm):
    rating = FloatField(label="Enter your rating", validators=[DataRequired()])
    review = StringField(label="Enter your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

# Add Movie Form
class AddForm(FlaskForm):
    title = StringField(label="Search Movie by Title", validators=[DataRequired()])

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movies(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    movies = Movies.query.all()
    return render_template("index.html", list_of_movies = movies)


@app.route("/add", methods = ["GET", "POST"])
def add_movie():
    add_form = AddForm()
    return render_template("add.html", form = add_form)

@app.route("/edit", methods = ["GET", "POST"])
def update():
    update_form = UpdateForm()
    if request.method == "POST":
        movie_to_update = db.get_or_404(Movies, request.args["id"])
        movie_to_update.rating = update_form.data["rating"]
        movie_to_update.review = update_form.data["review"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form = update_form)

@app.route("/<id>")
def delete(id):
    movie_to_delete = db.get_or_404(Movies, ident=id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
