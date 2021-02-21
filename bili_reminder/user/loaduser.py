import requests as rs
import json
from ..config import HEAD
from . import upmaster


def parse_response_for_upmater(response: dict) -> list:
    ulist = response['data']['list']
    if len(ulist) == 0:
        raise upmaster.AudienceFollowingListEmptyError(
            'This audience have not following any upmaster!')
    return ulist


def get_response_for_upmater(uid, pn) -> dict:
    url = r'http://api.bilibili.com/x/relation/followings?vmid={}&pn={}'.format(
        uid, pn)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    return rjson


def parse_response_to_upmater_list(uid, pn=1) -> list:
    return parse_response_for_upmater(get_response_for_upmater(uid, pn))


def parse_response_for_audience(response: dict) -> upmaster.Audience:
    if response['code'] == -404:
        raise upmaster.UserNotExistError('This user does not exist!')
    udict = response['data']['card']
    return upmaster.Audience.parse_audience_response(udict)


def get_response_for_audience(uid) -> dict:
    url = r'http://api.bilibili.com/x/web-interface/card?mid={}'.format(uid)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    return rjson


def parse_response_to_audience(uid) -> upmaster.Audience:
    return parse_response_for_audience(get_response_for_audience(uid))
