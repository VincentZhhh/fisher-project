from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合逻辑')])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空'), Length(6, 23)])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多十个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')



class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合逻辑')])
    password = PasswordField(validators=[
        DataRequired(message='密码不能为空'), Length(6, 23)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合逻辑')])

class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输出的密码不相同')
    ])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6, 32)])