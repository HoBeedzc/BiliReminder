import time
from .user.loaduser import parse_response_to_audience
from .config import BILIBILI_UID, SLEEP_TIME
from .reminder.mail import BiliNoticeMail


class BiliReminder:
    def __init__(self):
        pass

    def create_origin_user(self):
        self.ouser = parse_response_to_audience(BILIBILI_UID)

    def get_origin_user_following_list(self):
        self.ouser.get_following_list()

    def Notice_begin_monitor_info(self):
        BiliNoticeMail.send_ready_mail()

    def start(self):
        self.create_origin_user()
        self.get_origin_user_following_list()
        self.Notice_begin_monitor_info()
        while True:
            self.ouser.update_following_list_manuscript()
            time.sleep(SLEEP_TIME)
        pass
