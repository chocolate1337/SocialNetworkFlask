from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
							   Length, EqualTo)

from models import User

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('Пользователь с таким именем уже существует.')

def email_exists(form,field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('Пользователь с такой почтой уже существует.')

class RegisterForm(Form):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message = ("Имя пользователя должно состоять только из одного слова, букв, цифр и подчеркиваний")
				),
			name_exists
		])

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists
		])

	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=2),
			EqualTo('password2', message = 'Пароль должен быть больше')
		])
	password2 = PasswordField(
		'Подтверждение пароля',
		validators=[DataRequired()
		])


class LoginForm(Form):
	email = StringField('Почта', validators=[DataRequired(), Email()])
	password = PasswordField('Пароль', validators=[DataRequired()])

class PostForm(Form):
	content = TextAreaField("Как дела?", validators = [DataRequired()])