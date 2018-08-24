from flask import jsonify, request
from flask import render_template
from flask import flash
from flask import url_for
from flask_login import current_user

from app.froms.book import SearchBook
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.trade import TradeInfo
from app.web import web
from app.view_models.book import BookCollection, BookViewModel
import json


@web.route('/book/search')
def search():
    # q = request.args['q']
    # page = request.args['page']
    print(request.headers)
    form = SearchBook(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        book = YuShuBook()
        if isbn_or_key == 'isbn':
            book.search_by_isbn(q)
            # res = YuShuBook.search_by_isbn(q)
        else:
            book.search_by_keyword(q, page)
            # res = b'str(res)'.decode('utf-8')
            # res = eval(res)
        books.fill(book, q)

    else:
        # return jsonify({'msg': '参数校验失败'})
        flash('搜索错误')
    # return json.dumps(books, default=lambda o: o.__dict__)
    return render_template('search_result.html', books=books)


@web.route('/test')
def test():
    flash('this is a flash')
    return render_template('test1.html')


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template("book_detail.html", book=book, gifts=trade_gifts_model,
                           wishes=trade_wishes_model, has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)




