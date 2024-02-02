from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# CREATE FORM
class BlogForm(FlaskForm):
    title = StringField(label="Enter the title of your Blog Post", validators=[DataRequired()])
    subtitle = StringField(label="Enter a subtitle for your blogpost", validators=[DataRequired()])
    author = StringField(label="Enter the name of author", validators=[DataRequired()])
    body = CKEditorField(label="Edit your blog", validators=[DataRequired()])
    img_url = StringField(label="Enter an img url", validators=[DataRequired(), URL(require_tld = True)])
    submit = SubmitField(label="Add blog")
    
with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, ident=post_id)
    print(requested_post)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods = ["GET", "POST"])
def add_new_post():
    add_blog_post = BlogForm()
    print(add_blog_post.data)
    if add_blog_post.validate_on_submit():
        date = datetime.now().strftime('%B %d, %Y')
        print(date)
        title = add_blog_post.data["title"]
        subtitle = add_blog_post.data["subtitle"]
        author = add_blog_post.data["author"]
        body = add_blog_post.data["body"]
        img_url = add_blog_post.data["img_url"]
        new_blog_post = BlogPost(title = title,
                                author = author,
                                body = body,
                                subtitle = subtitle,
                                date = date,
                                img_url = img_url)
        db.session.add(new_blog_post)
        db.session.commit()
        print("Successfully added the blog post")

    return render_template("make-post.html", form = add_blog_post)

# TODO: edit_post() to change an existing blog post
@app.route("/edit_post", methods = ["GET", "PUT"])
def edit_post():
    
# TODO: delete_post() to remove a blog post from the database
@app.route("/delete_post")
# Below is the code from previous lessons. No changes needed.
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
