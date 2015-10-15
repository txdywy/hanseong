# -*- coding: utf-8 -*-
import datetime, time
from models import *

class User(Base):
    __tablename__ = 'user'
    POWER_ADMIN = 2**9

    id = Column(Integer, primary_key=True)
    email = Column(String(128), index=True)
    phone = Column(String(32), index=True)
    qq = Column(String(32), default='')
    wx = Column(String(32), default='')
    wb = Column(String(32), default='')
    yy = Column(String(32), default='')
    alipay = Column(String(32), default='')
    pw_hash = Column(String(128))
    name = Column(String(32), index=True)
    power = Column(Integer, default=0)
    sex = Column(String(16), default='')
    age = Column(Integer, default=18)
    address = Column(Text, default='')
    icon = Column(String(512), default='')
    profile = Column(String(512), default='')
    city = Column(String(50), default='')
    create_time = Column(DATETIME(), default=datetime.datetime.now())
    update_time = Column(DATETIME(), default=datetime.datetime.now())


    def __repr__(self):
        return '<User %r>' % (self.id)
