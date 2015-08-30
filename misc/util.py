import smtplib
import email.utils
from email.mime.text import MIMEText
import functools
import qiniu

try:
    from config import HANSEONG_HOST
except Exception, e:
    print '==============no HANSEONG_HOST set, ues hanseong.xx as default==============', e
    HANSEONG_HOST = 'hanseong.ml'
HANSEONG_SUPPORT = 'support@%s' % HANSEONG_HOST

def makes(s):
    if type(s)==unicode:
        return s.encode('utf8','ignore')
    else:
        return s

def makeu(s):
    if type(s)==str:
        return s.decode('utf8','ignore')
    else:
        return s

def ex(func):
    @functools.wraps(func)
    def foo(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception, e:
            print '===================send email ex================', e
    return foo

@ex
def send_email(title, content, addr_to, addr_fr=None):
    # Create the message
    if not addr_fr:
        addr_fr = ALANCER_SUPPORT   
    msg = MIMEText(makes(content), 'html')
    msg['To'] = email.utils.formataddr(('Recipient', addr_to))
    msg['From'] = email.utils.formataddr(('Airbb', addr_fr))
    msg['Subject'] = title
    try:
        server = smtplib.SMTP('localhost')
    except Exception, e:
        print 'no SMTP service available', e
        return
    
    #server.set_debuglevel(True) # show communication with the server
    try:
        server.sendmail(addr_fr, [addr_to], msg.as_string())
    finally:
        server.quit()
