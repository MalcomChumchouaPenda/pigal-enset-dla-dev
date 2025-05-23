
from collections import OrderedDict


class Entry:

    def __init__(self, id, text, 
                 parentid=None,
                 endpoint=None, 
                 url=None,
                 rank=0,
                 icon=None):
        super().__init__()
        self.id = id
        self.text = text
        self.parentid = parentid
        self.endpoint = endpoint
        self.url = url
        self.rank = rank
        self.icon = icon
        self.children = OrderedDict()

    def add(self, id, text, endpoint=None, url=None, rank=0, icon=None):
        entry = Entry(id, text, parentid=self.id, 
                      endpoint=endpoint, url=url,
                      rank=rank, icon=icon)
        self.children[id] = entry
        return entry

    def to_dict(self):
        data = {'id':self.id,
                'text':self.text,
                'parentid':self.parentid,
                'endpoint':self.endpoint,
                'url':self.url,
                'rank':self.rank,
                'icon':self.icon,
                'children':[]
                }

        f = lambda x: (x.rank, x.text)
        for child in sorted(self.children.values(), key=f):
            data['children'].append(child.to_dict())
        return data


navbar = Entry('navbar', 'navbar')
sidebar = Entry('sidebar', 'sidebar')
BARS = [navbar, sidebar]

