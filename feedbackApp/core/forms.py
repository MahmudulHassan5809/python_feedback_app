from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField,RadioField
from wtforms.validators import DataRequired


class FeedBackForm(FlaskForm):
	customer = StringField('Customer Name',validators=[DataRequired()])
	dealer = SelectField(
  		'Select Dealer',
        choices=[('Tom Smith', 'Tom Smith'), ('Karen Swanson', 'Karen Swanson'), ('Jim Johnson', 'Jim Johnson'),('Shauna Gifford', 'Shauna Gifford')],validators=[DataRequired()]
    )
	rating = RadioField('Rating', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')],validators=[DataRequired()])

	comments  = TextAreaField('Comments about your experience',validators=[DataRequired()])

	submit = SubmitField("Submit")

