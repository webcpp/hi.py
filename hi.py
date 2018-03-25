from functools import wraps
from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
import re
import sys

__author__ = 'pangpang@hi-nginx.com'
__version__ = '0.1.2'
__license__ = 'GNU GENERAL PUBLIC LICENSE ,Version 3, 29 June 2007'

reload(sys)

sys.setdefaultencoding('utf-8')


class hi:
    def __init__(self):
        self.uri_map = {}
        self.uri_regex_map = {}

    def route(self, pattern, method):
        def wrapper_a(func):
            self.uri_map[pattern] = {'method': method, 'callback': func}
            self.uri_regex_map[pattern] = re.compile(pattern)

            @wraps(func)
            def wrapper_b(req, res, param):
                func(req, res, param)
            return wrapper_b
        return wrapper_a

    def run(self, req, res):
        for k, v in self.uri_map.items():
            if req.method() in v['method']:
                m = self.uri_regex_map[k].match(req.uri())
                if m:
                    v['callback'](req, res, m.groupdict())
                    break


class template:
    def __init__(self, template_search_path):
        self.templates_dir = template_search_path
        self.jinja2_env = Environment(loader=FileSystemLoader(
            self.templates_dir), autoescape=select_autoescape(['htm', 'html', 'xml', 'json']))

    def file_render(self, template_file, variable):
        engine = self.jinja2_env.get_template(template_file)
        result = engine.render(variable)
        return str(result)

    def string_render(self, template_string, variable):
        engine = Template(template_string)
        result = engine.render(variable)
        return str(result)
