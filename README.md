# hi.py
python web framework for hi-nginx

## hello world

```python

from hi import hi,template
import os

app =hi()

@app.route(r'^/test/?$',['GET'])
@app.route(r"^/$",['GET'])
def hello_world(req,res,param):
    res.header('Content-Type','text/plain;charset=utf-8')
    res.content('hello,world')
    res.status(200)

@app.route(r"^/client/?$",['GET','POST'])
def client(req,res,param):
    res.content('{}<br>{}<br>{}<br>{}<br>{}'.format(req.client(),req.method(),req.uri(),req.user_agent(),req.param()))
    res.status(200)

@app.route(r"^/hello/(?P<who>\w+)?$",['GET'])
def hello(req,res,param):
    res.content('{}={}'.format('who',param['who']))
    res.status(200)

@app.route(r'^/template/(?P<name>\w+)/(?P<age>\d+)/?$',['GET'])
def tpl(req,res,param):
    param['title']='test jinja2 template'
    tpl_engine = template(os.path.join(os.getcwd(),'python/templates'))
    res.content(tpl_engine.file_render('b.html',param))
    res.status(200)


if __name__ == '__main__':
    app.run(hi_req,hi_res)


```
- a.html

```html

<html>
	<head><title>{{ title }}</title></head>
	<body>Hello {{ name }},you are {{ age }} years old.</body>
</html>


```

- b.html

```html

{% extends 'a.html'  %}
{% block body %}
	{{ super()  }}
	继承
{{ name  }} is {{ age }} years old.
{% endblock %}


```
