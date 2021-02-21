from . import manuscript
from ..user import upmaster
import requests as rs
import json
from ..config import HEAD


def parse_response_for_manuscript(response: dict) -> manuscript.Manuscript:
    vlist = response['data']['list']['vlist']
    if len(vlist) == 0:
        raise upmaster.UpMasterLastManuscriptEmptyError(
            'This UpMater have not upload a manuscript!')
    else:
        manuscript_response = vlist[0]
    return manuscript.Manuscript.parse_manuscript_response(manuscript_response)


def get_response_for_manuscript(uid) -> dict:
    url = r'http://api.bilibili.com/x/space/arc/search?mid={}&pn=1&ps=1'.format(
        uid)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    return rjson


def parse_response_to_manuscript(uid) -> manuscript.Manuscript:
    return parse_response_for_manuscript(get_response_for_manuscript(uid))
