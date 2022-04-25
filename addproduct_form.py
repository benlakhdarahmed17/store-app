from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField
from wtforms.validators import InputRequired

class addproduct(FlaskForm):  
    name = StringField('Product name', validators=[InputRequired()])
    quantity = IntegerField('Quantity', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    category = StringField('Category', validators=[InputRequired()])
    description = StringField('Desciption', validators=[InputRequired()])
    image = FileField('Product image')
    submit = SubmitField('Submit')