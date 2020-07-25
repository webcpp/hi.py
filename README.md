# hi.py
python web framework for hi-nginx

## hello world

```nginx
	location ~ \.py$ {
		hi_need_cache off;
		hi_cache_expires 5s;
		hi_need_cookies off;
		hi_need_session off;
		hi_session_expires 300s;
		hi_python_script python/index.py;
	}

```

```python

# -*- coding: utf-8 -*-

from hi import hi,template
import os

app =hi()

@app.route(r'^/(test|hello)\.py/?$',['GET'])
def hello_world(req,res,param):
    res.header('Content-Type','text/plain;charset=utf-8')
    res.content('hello,world')
    res.status(200)

@app.route(r"^/client\.py/?$",['GET','POST'])
def client(req,res,param):
    res.content('{}<br>{}<br>{}<br>{}<br>{}'.format(req.client(),req.method(),req.uri(),req.user_agent(),req.param()))
    res.status(200)

@app.route(r"^/hello/(?P<who>\w+)?\.py$",['GET'])
def hello(req,res,param):
    res.content('{}={}'.format('who',param['who']))
    res.status(200)

@app.route(r'^/template/(?P<name>\w+)/(?P<age>\d+)/?\.py$',['GET'])
def tpl(req,res,param):
    param['title']='jinja2 template'
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
	<body>
    {% block body %}
    Hello {{ name }},you are {{ age }} years old.
    {% endblock %}
    </body>
</html>


```

- b.html

```html

{% extends 'a.html'  %}
{% block body %}
	{{ super()  }}
    <br />
	Hello {{ name }},you are {{ age }} years old.
{% endblock %}


```

## example

[pyexample](https://github.com/webcpp/pyexample)