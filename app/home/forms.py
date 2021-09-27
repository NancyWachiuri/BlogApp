from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo, ValidationError

class CategoryForm(FlaskForm):
    category = StringField('Your Email Address',validators=[Required()])
    submit = SubmitField('Add Category')