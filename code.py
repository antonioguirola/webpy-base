# -*- coding: utf-8 -*-

import re
import web
import config
import db
import forms
from view import *
from web.contrib.template import render_mako
from web import form

# Para poder usar sesiones con web.py
web.config.debug = False

urls = (
    '/', 'index'
)

app = web.application (urls, locals())

# Ejemplo uso de sesiones
# session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'usuario':'','username':''})


class index:
    def GET(self):
    	args={'title':u'Título'}            
    	return serve_template('index.html', **args)


      
if __name__ == "__main__":
    app.run()
    