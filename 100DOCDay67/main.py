from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# Flask Login Setup:
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    
    
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated )


@app.route('/register', methods = ["GET", "POST"])
def register():
    
    if request.method == "POST":
        new_user = User()
        new_user.name = request.form.get("name")
        new_user.email = request.form.get("email")
        new_user.password = generate_password_hash(password = request.form.get("password"),
                                                    salt_length=8)
        existing_email = db.session.execute(db.select(User).where(User.email == new_user.email)).scalar()
        if existing_email == None:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
        else:
            flash("You have already registered with that email.")
            return redirect(url_for('register'))
        
        return redirect(url_for('secrets'))
        
    return render_template("register.html")


@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        get_user_pw_by_email = db.session.execute(db.select(User).where(User.email == email)).scalar()
        
        if get_user_pw_by_email:
            if check_password_hash(pwhash = get_user_pw_by_email.password, password=password):
                user = db.session.execute(db.select(User).where(User.email == email))
                login_user(user = user.scalar())
                return redirect(url_for('secrets'))
            else:
                flash("Password incorrect, please try again.")
                return redirect(url_for('login'))
        else:
            flash("There email does not exist. Please try again.")
            return redirect(url_for('login'))

        
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", username = current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
