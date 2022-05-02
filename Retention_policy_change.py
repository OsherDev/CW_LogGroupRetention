# Py - 3.9 / timeout in 13 min 
import json
import boto3
import subprocess


client = boto3.client('logs')
newlist=[]

def lambda_handler(event, context):
    response = client.describe_log_groups()
    for logs in response['logGroups']:
        newlist.append(logs['logGroupName']) # get the first 50 log groups 
    while "nextToken" in response:
        response = client.describe_log_groups(nextToken=response["nextToken"])   # Token for get more than just 50 log groups (limitation of aws) 
        for logs in response['logGroups']:
            newlist.append(logs['logGroupName'])
    for i in newlist:
        if 'Int' in i or 'inegration' in i:
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=30
            )
        elif 'stage' in i or 'Stg' in i or 'Staging' in i:
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=90          
            )
        elif 'Prod' in i or 'Prd' in i or 'production' in i:
            log=client.put_retention_policy(
                logGroupName=i,
                retentionInDays=180
            )
