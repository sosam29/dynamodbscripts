import boto3
import json
import decimal

from botocore.exceptions import ClientError

dyndb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:8000')

table = dyndb.Table('Items2')

try:
    for i in range(20, 40):
        response= table.put_item(
        Item={
            'Id':i,
            'Name': 'Item ' + str(i)
            }
        )

    print("Put Item Succedded")
    print(response)
    print(json.dumps(response, indent=4))
except Exception as err:
    print(err)