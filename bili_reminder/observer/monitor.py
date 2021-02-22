from . import manuscript
from ..user import upmaster
import requests as rs
import json
from ..config import HEAD


def parse_response_for_manuscript(response: dict) -> manuscript.Manuscript:
    if response['code'] == -412:
        print('请求被拦截，请稍后再试！')
        exit()
    vlist = response['data']['list']['vlist']
    if len(vlist) == 0:
        # raise upmaster.UpMasterLastManuscriptEmptyError(
        #     'UpMater {} have not upload a manuscript!'.format(response['uid']))
        manuscript_response = {
            'bvid': -1,
            'title': None,
            'mid': response['uid']
        }
    else:
        manuscript_response = vlist[0]
    return manuscript.Manuscript.parse_manuscript_response(manuscript_response)


def get_response_for_manuscript(uid) -> dict:
    url = r'http://api.bilibili.com/x/space/arc/search?mid={}&pn=1&ps=1'.format(
        uid)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    rjson['uid'] = uid
    return rjson


def parse_response_to_manuscript(uid) -> manuscript.Manuscript:
    return parse_response_for_manuscript(get_response_for_manuscript(uid))
