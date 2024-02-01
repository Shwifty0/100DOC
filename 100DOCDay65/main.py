from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random


app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods = ["GET"])
def random_cafe():
    random_cafe = random.choice(Cafe.query.all())
    
    return jsonify(cafe = random_cafe.to_dict())

@app.route("/all", methods = ["GET"])
def all_cafes():
    all_cafes = Cafe.query.all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args["loc"]
    cafes_at_location = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    if cafes_at_location:
        cafes_at_location = cafes_at_location.scalars().all()
        return jsonify(cafes = [cafe.to_dict() for cafe in cafes_at_location])
    else:
        return jsonify(error = {"Not Found": "Sorry we don't have a cafe at that location"})
    
# HTTP POST - Create Record
@app.route("/add", methods = ["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url= request.form.get("map_url"),
        img_url= request.form.get("img_url"),
        location= request.form.get("location"),
        seats= request.form.get("seats"),
        has_toilet= bool(request.form.get("has_toilet")),
        has_wifi= bool(request.form.get("has_wifi")),
        has_sockets= bool(request.form.get("has_sockets")),
        can_take_calls= bool(request.form.get("can_take_calls")),
        coffee_price= request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    
    return jsonify(response = {"success":"Successfully added the new cafe"})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods = ["PATCH"])
def update_price(cafe_id):
    get_cafe_with_id = db.session.get(Cafe, ident=cafe_id)
    if get_cafe_with_id:
        get_cafe_with_id.coffee_price = request.args.get("price")
        db.session.commit()
        return jsonify(response = {"success":"Successfully updated the price."}), 200
    else:
        return jsonify(response = {"Not Found":"Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
