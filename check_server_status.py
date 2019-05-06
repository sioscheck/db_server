import logging
import boto3
from boto3.session import Session

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# set your access key here, don't use my key!!
AWS_ACCESS_KEY = 'AKIAJTC8RTDGMGIRHH4A'
# set your secret access key here, don't use my key!!
AWS_ACCESS_SECRET = '9Z/jzN1C+hauz8f2hwroL9ABmx06wr/EjnNgucEc'

# option
AWS_REGION = 'ap-northeast-1'
EC2_TARGET_NAME_TAG = 'TestTarget'

def handler(event, context):
