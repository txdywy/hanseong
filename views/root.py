# -*- coding: utf-8 -*-
from views import *
from flask import (Blueprint, current_app, request, g, url_for, make_response,
                   render_template, redirect, jsonify)
from models.model_test import TestUser, flush
from wsgi import app
from misc import qiniu_agent
import simplejson as json


@app.route('/style')
def style():
    return render_template('test/style.html')


@app.route('/creative')
def creative():
    return render_template('test/creative.html')


@app.route('/gray')
def gray():
    return render_template('test/gray.html')


@app.route('/qn')
def qn():
    return render_template('test/qn.html')


@app.route('/uptoken')
def uptoken():
    d = {'uptoken': qiniu_agent.get_qn_token()}
    return json.dumps(d)


@app.route('/map_test')
def map_test():
    return render_template('test/map.html')


@app.route('/map_<name>')
def map_name(name):
	return render_template('test/map_%s.html' % name)


@app.route('/m')
def m():
    lat, lng = '29.7604267', '-95.3698028'
    return render_template('test/m.html', lat=lat, lng=lng)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/no')
def no():
    return render_template('no.html')


@app.route('/lay')
def lay():
    return render_template('layout.html')


def de(x):
    return x.decode('utf8')


BOOK_READ_LIST = [(de('제1과 취미'), [(de('1. 노벨 이야기'), 'http://ac-9dv47dhd.clouddn.com/2be466026cef44c2.pdf'), 
                                     (de('2. 세계인의 취미'), 'http://ac-9dv47dhd.clouddn.com/3c7650998860ef6c.pdf'), 
                                     (de('3. 수집광 가족'), 'http://ac-9dv47dhd.clouddn.com/c5460f1f2f980779.pdf'),
                                    ]
                  ),
                  ]


@app.route('/menu')
def menu():
    try:
        bid = request.args.get('bid')
    except Exception, e:
        print '===========', e
        return render_template('no.html')
    if bid == 'read3':
        return render_template('menu.html', data=BOOK_READ_LIST)
    else:
        return render_template('no.html')








