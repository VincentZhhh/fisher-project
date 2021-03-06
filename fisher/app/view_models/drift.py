from app.libs.enum import PendingStatus


class DriftCollection:
    def __init__(self, drifts, current_user_id):
        self.data = []
        self._parse(drifts, current_user_id)

    def _parse(self, drifts, current_user_id):
        for drift in drifts:
            temp = DriftViewModel(drift, current_user_id)
            self.data.append(temp.data)

class DriftViewModel:
    def __init__(self, drift, current_user_id):
        self.data = {}

        self.data = self._parse(drift, current_user_id)

    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        if drift.requester_id == current_user_id:
            you_are = 'requester'
        else:
            you_are = 'gifter'
        return you_are

    def _parse(self, drift, current_user_id):
        you_are = self.requester_or_gifter(drift, current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            'you_are': you_are,
            'drift_id': drift.id,
            'book_title': drift.book_title,
            'book_author': drift.book_author,
            'book_img': drift.book_img,
            'date': drift.create_datetime.strftime('%Y-%m-%d'),
            'message': drift.message,
            'address': drift.address,
            'recipient': drift.recipient_name,
            'mobile': drift.mobile,
            'status': drift.status,
            'operator': drift.requester_nickname if you_are != 'requester'\
                else drift.gifter_nickname,
            'status_str': pending_status,
        }
        return r