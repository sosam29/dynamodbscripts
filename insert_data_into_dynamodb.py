import boto3
import json

dyndb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:8000')

table = dyndb.Table('Items')
for i in range(1,20):
    response= table.put_item(
        Item={
            'Id':i
            }
        )

print("Put Item Succedded")
print(response)
print(json.dumps(response, indent=4))