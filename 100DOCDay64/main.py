from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests, os

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
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title:Mapped[int] = mapped_column(String, unique=True)
    year:Mapped[int] = mapped_column(Integer)
    description:Mapped[int] = mapped_column(String)
    rating:Mapped[int] = mapped_column(Float, nullable=True)
    ranking:Mapped[int] = mapped_column(Integer,nullable=True)
    review:Mapped[int] = mapped_column(String, nullable=True)
    img_url:Mapped[int] = mapped_column(String)

# Edit Rating and Review FlaskForm
class UpdateForm(FlaskForm):
    rating = FloatField(label="Enter your rating", validators=[DataRequired()])
    review = StringField(label="Enter your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")

# Add Movie Form
class AddForm(FlaskForm):
    title = StringField(label="Search Movie by Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie", validators=[DataRequired()])

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars() # orderby sorts in ascending by default
    ranked_movies = movies.all()
    for i in range(len(ranked_movies)):
        ranked_movies[i].ranking = len(ranked_movies) - i
    db.session.commit()
        
    return render_template("index.html", list_of_movies = ranked_movies)


@app.route("/add", methods = ["GET", "POST"])
def add_movie():
    add_form = AddForm()
    search_movie_endpoint = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": os.environ.get("TMDB_API")
    }
    params = {
        "query": add_form.data["title"],
        "include_adult" : True,
    }
    
    if request.method == "POST":
        response = requests.get(search_movie_endpoint, params=params, headers=headers)
        return render_template("select.html", api_response = response.json()["results"])
    
    if request.args:
        selected_movie = request.args['movie_id']
        get_movie_details_endpoint = f"https://api.themoviedb.org/3/movie/{selected_movie}"
        response = requests.get(get_movie_details_endpoint, headers=headers)
        title = response.json()["original_title"]
        img_url = f"https://image.tmdb.org/t/p/w500{response.json()['poster_path']}"
        description = response.json()["overview"]
        year = response.json()["release_date"].split("-")[0]

        new_movie = Movies(title=title,
                            img_url=img_url,
                            description=description,
                            year=year
                        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("update", id = new_movie.id))
        
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
