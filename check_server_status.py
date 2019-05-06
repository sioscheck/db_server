import logging
import boto3
from boto3.session import Session

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# set your access key here, don't use my key!!
# set your secret access key here, don't use my key!!

# option

def handler(event, context):
