from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password= PasswordField(label="Password", validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField(label="Register")

# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField(label="Email", description='Enter your email here', validators=[DataRequired()])
    password = PasswordField(label="Password", description='Your Password', validators=[DataRequired()])
    submit = SubmitField(label="Login")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField(label="Comment", validators=[DataRequired()])
    submit_comment = SubmitField(label='Add comment')
    
# TODO: Email Functionality Form:
class ContactForm(FlaskForm):
    name = StringField(label="Your name", validators=[DataRequired()])
    email_address = StringField(label="your email", validators=[DataRequired()])
    phone_number = StringField(label="Your Phone Number", validators=[DataRequired()])
    message = StringField(label="Your message", validators=[DataRequired()])
    submit_comment = SubmitField(label='Send Message')