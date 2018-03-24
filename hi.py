import re

__author__ = 'pangpang@hi-nginx'
__version__ = '0.1.0'
__license__ = 'GNU GENERAL PUBLIC LICENSE ,Version 3, 29 June 2007'

class hi:
    def __init__(self):
        self.uri_map={}
        self.uri_regex_map={}

    def route(self,pattern,method):
        def wrapper_a(func):
            self.uri_map[pattern]={'method':method,'callback':func}
            self.uri_regex_map[pattern]=re.compile(pattern)
            def wrapper_b(req,res,param):
                func(req,res,param)
                return wrapper_b
        return wrapper_a

    def run(self,req,res):
        for k,v in self.uri_map.items():
            if req.method() in v['method']:
                m=self.uri_regex_map[k].match(req.uri())
                if m:
                    v['callback'](req,res,m.groupdict())
                    break

