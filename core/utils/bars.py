
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


navbar = _NavBar()
