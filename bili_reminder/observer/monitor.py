from . import manuscript
from ..user.upmaster import UpMasterLastManuscriptEmptyError
import requests as rs
import json
from ..config import HEAD


def parse_response(response: dict) -> manuscript.Manuscript:
    vlist = response['data']['list']['vlist']
    if len(vlist) == 0:
        raise UpMasterLastManuscriptEmptyError(
            'This UpMater have not upload a manuscript!')
    else:
        manuscript_response = vlist[0]
    return manuscript.Manuscript.parse_manuscript_response(manuscript_response)


def get_response(uid) -> dict:
    url = r'http://api.bilibili.com/x/space/arc/search?mid={}&pn=1&ps=1'.format(
        uid)
    r = rs.get(url, headers=HEAD)
    rjson = json.loads(r.content.decode('utf-8'))
    return rjson


def parse_response_to_manuscript(uid) -> manuscript.Manuscript:
    return parse_response(get_response(uid))


if __name__ == '__main__':
    uid = 246546608
    print(parse_response_to_manuscript(uid))
