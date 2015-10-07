from config import *
from qiniu import Auth
try:
    q = Auth(QN_ACCESS_KEY, QN_SECRET_KEY)
except:
    print '======no qn========'
bucket_name = 'udon'

def get_qn_token():
    return q.upload_token(bucket_name)
