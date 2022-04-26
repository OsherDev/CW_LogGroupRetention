import json
import boto3

client = boto3.client('logs')
newlist=[]

def lambda_handler(event, context):
    response = client.describe_log_groups()
    for logs in response['logGroups']:
        newlist.append(logs['logGroupName'])
    print(len(response['logGroups']))
    for i in newlist:
        if "Int" in i:
            print(i)
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=30
            )
        elif "stg" in i:
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=90          
            )
        elif "prod" in i:
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=180
            )
