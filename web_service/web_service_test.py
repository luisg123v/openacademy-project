# -*- coding: utf-8 -*-

import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
sessions = call('openacademy.session','search_read', [], ['name','seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

# 3.create a new session
duplicates = call('openacademy.session','search_count', [('name', '=', 'My session')])
if not duplicates:
    session_id = call('openacademy.session', 'create', {
        'name' : 'My session',
        'course_id' : 2,
    })
else:
    print "The session 'My session' already exists, not created."
