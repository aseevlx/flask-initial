from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import required
from models import User


class SimpleForm(FlaskForm):
    u = User.query.all()
    users = [(user.id, user.name) for user in u]

    user = SelectField('name', choices=sorted(users, key=lambda usr: usr[1]), coerce=int)
    device = StringField('device', validators=[required()])