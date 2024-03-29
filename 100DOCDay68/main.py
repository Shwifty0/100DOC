from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, ContactForm
from smtplib import SMTP
import hashlib
import os



def gravatar_url(email, size=100, rating='g', default='retro', force_default=False):
    """
    This is a simple fucntion that hits the Gravatar endpoint with emails stored in the database
    allowing users to have different avatar images.
    
    """
    hash_value = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return f"https://www.gravatar.com/avatar/{hash_value}?s={size}&d={default}&r={rating}&f={force_default}"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Config for Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, ident=user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CONFIGURE TABLES
# TODO: Create a User table for all your registered users.
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id")) 
    author = relationship("User", back_populates = "posts")
    comments = relationship("Comment", back_populates="parent_post")
    
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class Comment(db.Model):
    __tablename__ = "comments"
    id = mapped_column(Integer, primary_key=True)
    text = mapped_column(Text, nullable=False)
    
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # Child Relationship to the BlogPosts
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")



with app.app_context():
    db.create_all()

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"The current user_id is: {current_user.get_id()} -- {type(current_user.get_id())}")
        admins = ["1", "2"]
        if current_user.get_id() in admins:
            return func(*args, **kwargs)
        else:
            return abort(403)
    return wrapper


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods = ["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        email = register_form.data["email"]
        password = register_form.data["password"]
        name = register_form.data["name"]

        hashed_password = generate_password_hash(password=password, salt_length=8)

        new_user = User(email = email,
                        password = hashed_password,
                        name = name)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            print("U are logged in!")
            return redirect(url_for("get_all_posts"))
        
        except:
            pass

    return render_template("register.html", form = register_form)


# TODO: Retrieve a user from the database based on their email.
@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.data['email']
        find_email_db = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if find_email_db and check_password_hash(find_email_db.password, login_form.data['password']):
            login_user(find_email_db)
            return redirect(url_for("get_all_posts"))
        else:
            flash("Register or enter your credentials correctly.")
            return redirect(url_for("login"))

    return render_template("login.html", form = login_form)

@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    admins = ["1", "2"]
    print(current_user.get_id())
    return render_template("index.html",
                            all_posts=posts,
                            logged_in = current_user.is_authenticated,
                            id = current_user.get_id(),
                            author = current_user,
                            admins = admins)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))



# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods = ["GET", "POST"])
def show_post(post_id):
    
    """
    This view has something to do with Relational Databases
    because what I am trying to achieve is only possible with one user
    the comment made by a user at a specific time will be rendered,
    but lets say if some1 else was logged in there would be no way to create a new comment because
    the database doesn't know how to relate the new user's comment
    """
    requested_post = db.get_or_404(BlogPost, post_id)
    comments = db.session.execute(db.select(Comment).where(Comment.post_id == post_id)).scalars().all()
    print(comments)
    comment_form = CommentForm()

    
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comment()
            new_comment.text = comment_form.data["comment"]
            new_comment.author_id = int(current_user.get_id())
            new_comment.post_id = post_id
            db.session.add(new_comment)
            db.session.commit()
            
            return redirect(url_for("show_post", post_id = post_id))
        else:
            flash("You have to login in order to comment")
            return redirect(url_for("login"))
    
    return render_template("post.html", 
                            post=requested_post,
                            form = comment_form,
                            logged_in = current_user.is_authenticated,
                            comments = comments,
                            gravatar_url = gravatar_url)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    
    return render_template("make-post.html", form=form, logged_in = current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, logged_in = current_user.is_authenticated)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))



@app.route("/about")
def about():
    return render_template("about.html", logged_in = current_user.is_authenticated)


@app.route("/contact", methods = ["GET", "POST"])
def contact():
    contact_form = ContactForm()
    msg_sent = False
    if contact_form.validate_on_submit():
        msg_sent = True
        with SMTP(host="smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(user="ozairmohammad12@gmail.com", password = os.environ.get("GMAIL_APP"))
            connection.sendmail(from_addr="ozairmohammad12@gmail.com", to_addrs = "ozairmohammad12@gmail.com",
                                msg=f"Subject:Someone Wants to Contact You!\n\nTheir email: {contact_form.data['email_address']}\nTheir name: {contact_form.data['name']}\nTheir message: {contact_form.data['message']}")
    
    return render_template("contact.html", form = contact_form, msg_sent = msg_sent)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
