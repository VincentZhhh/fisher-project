import threading
import time
from werkzeug.local import Local


# class A:
#     a = 'kiss'
#
#
# my_obj = Local()
# my_obj.b = 1
# print(my_obj.b)
#
#
# def worker():
#     my_obj.b = 2
#     print(my_obj.b)
#
#
# new_t = threading.Thread(target=worker, name='v_thread')
# new_t.start()
# time.sleep(1)
# print(my_obj.b)

class TestSetter():
    def __init__(self):
        self.name = ''
        self.age = 18
        self.school = 'bnuz'
        self._sex = 'male'

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, r):
        self.name = 'hello zws'
        self._sex = r+'sex'

t = TestSetter()
t.name = 'zws'
print(t.name)
print(t._sex)
t.sex = 'hello'
print(t._sex)
print(t.name)



