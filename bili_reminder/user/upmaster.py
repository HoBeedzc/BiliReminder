from ..observer.monitor import parse_response_to_manuscript
from .loaduser import parse_response_to_upmater_list


class UserError(ValueError):
    pass


class AudienceFollowingListEmptyError(UserError):
    pass


class UpMasterLastManuscriptEmptyError(UserError):
    pass


class User:
    """
    """
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        pass

    def __str__(self):
        return '{},{}'.format(self.uid, self.name)


class UpMaster(User):
    """
    """
    def __init__(self, uid, name):
        super().__init__(uid, name)
        self.last_manuscript = None

    def update_reminder(self):
        pass

    def get_last_manuscript(self):
        new_last_manuscript = parse_response_to_manuscript(self.uid)
        if self.last_manuscript is None:
            self.last_manuscript = new_last_manuscript
        elif self.last_manuscript != new_last_manuscript:
            self.last_manuscript = new_last_manuscript
            self.update_reminder()
        else:
            pass

    @classmethod
    def parse_upmaster_response(cls, response: dict):
        uid = response['mid']
        name = response['uname']
        return cls(uid, name)


class Audience(User):
    """
    """
    def get_following_list(self):
        self.following_list = []
        for pn in range(1, 6):
            response = parse_response_to_upmater_list(pn=pn)
            for upmaster_info in response:
                self.following_list.append(
                    UpMaster.parse_upmaster_response(upmaster_info))
