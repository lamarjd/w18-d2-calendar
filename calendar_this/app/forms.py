from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    start_datetime = DateField("start_date", validators=[DataRequired()])
    start_datetime_t = TimeField("start_time", validators=[DataRequired()])
    end_datetime = DateField("end_date", validators=[DataRequired()])
    end_datetime_t = TimeField("end_time", validators=[DataRequired()])
    description = TextAreaField("description", validators=[DataRequired()])
    private = BooleanField("private")
    submit = SubmitField("Create an appointment")



