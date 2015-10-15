from fabric.api import * 
env.use_ssh_config = True
#env.hosts = ['sushi', 'polo', 'noodle']
def localhost():
    #env.use_ssh_config = False
    global run 
    run = local

def send(file):
    put(file, '~/')

def recv(file):
    get(file, './')

def nn():
    env.hosts = ['nn', ]

def pull():
    with cd('~/hanseong/'):
        run('git pull')

def restart():
    with cd('~/hanseong/'):
        run('supervisorctl restart hanseong')

def update_db():
    with cd('~/hanseong/'):
        run('openssl enc -des -d -a -in hanseong_db_enc -out hanseong.db')

def db():
    with cd('~/hanseong/'):
        run('./db_dec')

def init_db():
    with cd('~/hanseong/'):
        run("python -c 'from models.model_han import *;init_db()'")


def init_db():
    with cd('~/hanseong/'):
        run("python -c 'from models.model_test import *;init_db()'")

def free():
    run('free -mh')

def net():
    run('vnstat')
    run('vnstat -h')
    run('vnstat -d')
    run('vnstat -w')
    run('vnstat -m')

def fd():
    run('cat /proc/sys/fs/file-nr')

def dns(url):
    dns_server = ['', #local
                  '8.8.8.8', #Google
                  '8.8.4.4', #Google
                  '114.114.114.114', #ChinaTele
                  '4.2.2.2', #Legend
                  '208.67.222.222', #OpenDNS
                  '180.76.76.76', #Baidu
                  '223.5.5.5', #Ali
                  '223.6.6.6', #Ali
                  ]
    for dns in dns_server:
        run('nslookup %s %s' % (url, dns))

