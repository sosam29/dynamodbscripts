import boto3
import json
import decimal

from botocore.exceptions import ClientError

dyndb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:8000')

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o% 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

table = dyndb.Table('Items')

print("Attempting a conditional delete...")
id= 11
try:
    response = table.delete_item(
        Key={
            'Id': id
        }
    )
except ClientError as e:
    if e.response['Error']['Code'] == "ConditionalCheckFailedException":
        print(e.response['Error']['Message'])
    else:
        raise
else:
    print("DeleteItem succeeded:")
    print(json.dumps(response, indent=4, cls=DecimalEncoder))

