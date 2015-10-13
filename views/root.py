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


BOOK_READ_DICT = {3:[(de('제1과 취미'), [(de('1. 노벨 이야기'), 'http://ac-xm5nwdhd.clouddn.com/00b5cf83fc7b57f0.pdf'), 
                                     (de('2. 세계인의 취미'), 'http://ac-xm5nwdhd.clouddn.com/9b3f066f48688e75.pdf'), 
                                     (de('3. 수집광 가족'), 'http://ac-xm5nwdhd.clouddn.com/1a806d2924e869b8.pdf'),
                                    ]
                      ),
                     (de('제2과 일상'), [(de('1. 이사 떡'), 'http://ac-xm5nwdhd.clouddn.com/7725542566ad837c.pdf'), 
                                     (de('2. 우리 동네 슈퍼 이야기'), 'http://ac-xm5nwdhd.clouddn.com/04a128952f4c25d2.pdf'), 
                                     (de('3. 숫자'), 'http://ac-xm5nwdhd.clouddn.com/59c6d6b4920ab75d.pdf'),
                                    ]
                      ),
                     (de('제3과 건강'), [(de('1. 감기'), 'http://ac-xm5nwdhd.clouddn.com/25b6131788429d9c.pdf'), 
                                     (de('2. 화'), 'http://ac-xm5nwdhd.clouddn.com/88986611a6e29d30.pdf'), 
                                     (de('3. 느리게 살기'), 'http://ac-xm5nwdhd.clouddn.com/ef85847670995c2f.pdf'),
                                    ]
                      ),
                     (de('제4과 공연과 감상'), [(de('1. 담양 대나무 축제'), 'http://ac-xm5nwdhd.clouddn.com/04632c2fd767c469.pdf'), 
                                     (de('2. 1달러짜리 공연'), 'http://ac-xm5nwdhd.clouddn.com/3ae244c57ad93229.pdf'), 
                                     (de('3. 보는 그림, 읽는 그림'), 'http://ac-xm5nwdhd.clouddn.com/eb1fc1f30919f41a.pdf'),
                                    ]
                      ),
                     (de('제5과 사람'), [(de('1. 한국을 사랑한 언더우드'), 'http://ac-xm5nwdhd.clouddn.com/ac03eddafefe4693.pdf'), 
                                     (de('2. 바보 온달과 평강공주'), 'http://ac-xm5nwdhd.clouddn.com/7ae6b8544de7d5f8.pdf'), 
                                     (de('3. 아버지'), 'http://ac-xm5nwdhd.clouddn.com/d1a80e3f92c0926b.pdf'),
                                    ]
                      ),
                     (de('제6과 모임'), [(de('제6과 모임'), 'http://ac-xm5nwdhd.clouddn.com/01cd080617131e5f.pdf'), 
                                     (de('2.그 남자, 그 여자'), 'http://ac-xm5nwdhd.clouddn.com/0b7d47d8f1f922c1.pdf'), 
                                     (de('3.국경없는 의사회'), 'http://ac-xm5nwdhd.clouddn.com/6dfb1658c812e9e1.pdf'),
                                    ]
                      ),
                     (de('제7과 실수와 사과'), [(de('1. 오줌싸개'), 'http://ac-xm5nwdhd.clouddn.com/caaffd0ec7c640b2.pdf'), 
                                     (de('2. 실수에서 태어난 발명'), 'http://ac-xm5nwdhd.clouddn.com/2e9378e6e3a4c9ba.pdf'), 
                                     (de('3. 노란 손수건'), 'http://ac-xm5nwdhd.clouddn.com/457d3689f7fc8548.pdf'),
                                    ]
                      ),
                     (de('제8과 학교 생활'), [(de('1. 존경하는 선생님께'), 'http://ac-xm5nwdhd.clouddn.com/a25675acc4913cad.pdf'), 
                                     (de('2. 기적을 만든 선생님'), 'http://ac-xm5nwdhd.clouddn.com/80d1b1c3d73a87d3.pdf'), 
                                     (de('3. 서당 풍경'), 'http://ac-xm5nwdhd.clouddn.com/9f6ebe975abe2613.pdf'),
                                    ]
                      ),
                     (de('제9과 부탁과 거절'), [(de('1. 어머니의 마지막 부탁'), 'http://ac-xm5nwdhd.clouddn.com/c8964eca4dfb3987.pdf'), 
                                     (de('2. 관곡한 거절'), 'http://ac-xm5nwdhd.clouddn.com/7600d8ff1808bf23.pdf'), 
                                     (de('3. 부탁하는 광고'), 'http://ac-xm5nwdhd.clouddn.com/5ee43074a3f3f1be.pdf'),
                                    ]
                      ),
                     (de('제10과 어제와 오늘'), [(de('1. 한국 속의 외국인'), 'http://ac-xm5nwdhd.clouddn.com/87e4fad7b7c4d33a.pdf'), 
                                     (de('2. 재미있는 지명이야기'), 'http://ac-xm5nwdhd.clouddn.com/af442a5dd22eef6b.pdf'), 
                                     (de('3. 옛날에 쓰던 물건들'), 'http://ac-xm5nwdhd.clouddn.com/1b8150e294ad4696.pdf'),
                                    ]
                      ),
                      ]
                      }


@app.route('/menu')
def menu():
    try:
        bk = request.args.get('bk')
        bid = int(request.args.get('bid'))
    except Exception, e:
        print '===========', e
        return render_template('no.html')
    if bk == 'read':
        return render_template('menu.html', data=BOOK_READ_DICT[bid])
    else:
        return render_template('no.html')








