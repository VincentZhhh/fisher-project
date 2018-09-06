from flask import render_template, request, url_for, redirect, flash

from app.froms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm

from app.models.base import db
from app.models.user import User
from app.web import web
from flask_login import login_user, logout_user

__author__ = 'Mr.July'


@web.route('/register', methods=['GET', 'POST'])
def register():
    # print(request.method)
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
        # db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号密码不存在')
    return render_template('auth/login.html', form=form)
    


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            from app.libs.email import send_mail
            user = User.query.filter_by(email=form.email.data).first_or_404()
            send_mail(to=form.email.data, subject='重置你的密码', template='email/reset_password.html',
            user=user, token=user.generate_token())
            flash('重置链接已发送至您的邮箱')
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST':
        if form.validate():
            success = User.reset_password(token, form.password2.data)
            if success:
                flash('你的密码已重置')
                return redirect(url_for('web.login'))
            else:
                flash('密码重置失败')
    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))
