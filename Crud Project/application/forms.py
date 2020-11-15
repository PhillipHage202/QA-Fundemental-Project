from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, ValidationError
from application.models import Workout_plan, Session



class Workout_planForm (FlaskForm):
    name = StringField('Name',
        validators = [
            DataRequired(),
        ]    
    )
    submit = SubmitField('Submit')


class SessionForm(FlaskForm):
    pushups = IntegerField('Pushups', validators = [DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Add Session')


class OrderSessionForm(FlaskForm):
    order_with = SelectField('Order With',
        choices=[
            ("complete", "Completed"),
            ("id", "Recent"),
            ("old", "Old"),
            ('incomplete', "Incomplete")
        ]
    )
    submit = SubmitField('Order')