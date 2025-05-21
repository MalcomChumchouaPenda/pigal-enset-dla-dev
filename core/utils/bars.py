
from collections import OrderedDict


class Entry:

    def __init__(self, id, text, 
                 parentid=None,
                 endpoint=None, 
                 url=None,
                 rank=0):
        super().__init__()
        self.id = id
        self.text = text
        self.parentid = parentid
        self.endpoint = endpoint
        self.url = url
        self.rank = rank
        self.children = OrderedDict()

    def add(self, id, text, endpoint=None, url=None, rank=0):
        entry = Entry(id, text, parentid=self.id, 
                      endpoint=endpoint, url=url,
                      rank=rank)
        self.children[id] = entry
        return entry

    def to_dict(self):
        data = {'id':self.id,
                'text':self.text,
                'parentid':self.parentid,
                'endpoint':self.endpoint,
                'url':self.url,
                'rank':self.rank,
                'children':[]
                }

        f = lambda x: (x.rank, x.text)
        for child in sorted(self.children.values(), key=f):
            data['children'].append(child.to_dict())
        return data



class _NavBar:
    '''navbar of landing pages'''

    entries = [{
            'id':'home_menu',
            'text':'home_menu',
            'rank':0,
            'parentid':None,
            'children':[],
            'endpoint':None, 
            'url': None
        }]

    # def register_menu(self, id_):
    #     self.entries.append({
    #         'id':id_,
    #         'text':id_,
    #         'rank':0,
    #         'parentid':None,
    #         'children':[],
    #         'endpoint':None, 
    #         'url': None
    #     })
    
    @classmethod
    def add_entry(cls, parent, id_, text,
                  endpoint=None, url=None, 
                  rank=0):
        cls.entries.append({
            'id':id_,
            'text':text, 
            "rank":rank,
            'parentid':parent,
            'children':[],
            'endpoint':endpoint, 
            'url': url
        })
    
    
    # def register_domain(self, id_, text, rank=0):
    #     if id_ not in self.domains:
    #         domain = dict(id=id_, text=text, rank=rank, dashboards=[])
    #         self.domains[id_] = domain

    # def register_dashboard(self, domainid, id_, text, endpoint=None, url=None):
    #     dashboard = dict(id=id_, text=text, endpoint=endpoint, url=url)
    #     self.domains[domainid]['dashboards'].append(dashboard)

class SideBar:
    '''Sidebar of dashboard pages'''


# navbar = _NavBar()
navbar = Entry('home_menu', 'home_menu')
BARS = [navbar]

