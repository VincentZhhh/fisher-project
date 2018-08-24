# from app.models.user import User
import sys
#
from flask import Flask

sys.path.append('/home/vincent/桌面/天道酬勤/fisher')
# print(s)
print(sys.path)
from app.models.user import User

app = Flask('test')

@app.route('/')
def filter():
    # app_context.stack.push()
    r = User.query.filter_by(email='ubuntu@qq.com').all()
    print(r)
    print(type(r))
    return 'this is a sql test'

app.run(port=4096, host='0.0.0.0')