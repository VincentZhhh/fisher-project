from . import web
from app.view_models.book import BookViewModel
from app.models.gift import Gift
from flask import render_template


__author__ = 'Mr.July'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
