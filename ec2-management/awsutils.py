# awsutils

import boto3
def_session(region):
return boto3.session.Session(region_name=region)