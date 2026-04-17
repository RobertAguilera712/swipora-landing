from flask_wtf import FlaskForm
from app.models import  User
from wtforms import (
    StringField,
    DateField,
    IntegerField,
    SelectField,
    TelField,
    PasswordField,
    EmailField,
    FormField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    Regexp,
    Email,
    NumberRange,
    EqualTo,
    ValidationError
)
from datetime import date



class UserForm(FlaskForm):
    email = EmailField(label="Correo", validators=[DataRequired(), Email()])
    password = PasswordField(label="Contraseña", validators=[DataRequired()])


class NewUserForm(UserForm):
    title = "Usuario"
    confirm_password = PasswordField(
        label="Confirmar contraseña", validators=[DataRequired(), EqualTo("password")]
    )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Ya existe un usuario con ese correo.")