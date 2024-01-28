from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

# Define database schema
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title : Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)

# Initialize database with Flask App
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    books = Books.query.all()
    return render_template("index.html", all_books = books)


@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        add_book = Books(title = request.form["book_name"],
                        author = request.form["author"],
                        rating = request.form["rating"])
        db.session.add(add_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

