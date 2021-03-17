class Manuscript:
    """
    """
    def __init__(self, bvid, title, uid):
        self.bvid = bvid
        self.title = title
        self.uid = uid
        self.url = r"https://www.bilibili.com/video/{}".format(self.bvid)
        pass

    def __str__(self):
        manuscript_str = '{}'.format(self.title)
        return manuscript_str

    def __eq__(self, other):
        if self.bvid == other.bvid:
            if self.uid == other.uid:
                return True
        return False

    @classmethod
    def parse_manuscript_response(cls, response: dict):
        """
        """
        bvid = response['bvid']
        title = response['title']
        uid = response['mid']
        return cls(bvid, title, uid)
