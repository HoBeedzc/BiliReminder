import requests as rs
import json
from ..config import HEAD, BILIBILI_UID
from . import upmaster


def parse_response(response: dict) -> list:
    ulist = response['data']['list']
    if len(ulist) == 0:
        raise upmaster.AudienceFollowingListEmptyError(
            'This audience have not following any upmaster!')
    return ulist


def get_response(uid, pn) -> dict:
    url = r'http://api.bilibili.com/x/relation/followings?vmid={}&pn={}'.format(
        uid, pn)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    return rjson


def parse_response_to_upmater_list(uid=BILIBILI_UID, pn=1) -> list:
    return parse_response(get_response(uid, pn))
