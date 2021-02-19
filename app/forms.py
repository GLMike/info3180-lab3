from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    username = StringField('Username', 
                                validators=[DataRequired(), Length(min=2, max = 20)])

    email = StringField('Email', 
                                validators=[DataRequired(), Email()])

    subject = StringField('Subject',
    
                                validators= [DataRequired(), Length(min=1, max= 100)])
    
    message = TextAreaField('Message', 
                                validators=[DataRequired()])
    

