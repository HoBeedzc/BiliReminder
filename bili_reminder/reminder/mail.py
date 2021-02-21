from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from ..config import SMTP_SERVER, PORT, FROM_ADDR, PASSWD, TO_ADDR


class BiliNoticeMailError(ValueError):
    pass


class MessageEmptyError(BiliNoticeMailError):
    pass


class BiliNoticeMail:
    def __new__(cls, *args, **kwargs):
        if not hasattr(BiliNoticeMail, '_instance'):
            BiliNoticeMail._instance = object.__new__(cls, *args, **kwargs)
        return BiliNoticeMail._instance

    def __init__(self):
        self.server = SMTP_SSL(SMTP_SERVER, PORT)
        self.message = None
        pass

    def build_message(self, content: str):
        self.message = MIMEText(content, 'plain', 'utf-8')
        self.message['From'] = Header(FROM_ADDR, 'utf-8')
        self.message['To'] = Header(TO_ADDR, 'utf-8')
        self.message['Subject'] = Header('BiliReminder:Test', 'utf-8')

    def notice(self):
        if self.message is None:
            raise MessageEmptyError('Message is none!')
        self.server.login(FROM_ADDR, PASSWD)
        self.server.sendmail(FROM_ADDR, [TO_ADDR], self.message.as_string())
        self.message = None
        self.server.quit()

    @classmethod
    def send_notice_mail(cls, content):
        noticer = cls()
        noticer.build_message(content)
        noticer.notice()
        return noticer
