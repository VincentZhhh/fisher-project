from flask import Blueprint, render_template

from app.models.user import User

web = Blueprint('web', __name__)

@web.errorhandler(404)
def not_found(e):
    # r = User.query.filter_by(email='ubuntu@qq.com', status=1).all()
    # print(r[0].__dict__)
    # print(type(r[0]))
    return render_template('404.html')


