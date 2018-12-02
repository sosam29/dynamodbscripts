import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

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
# for i in range(1,20):
#     response= table.put_item(
#         Item={
#             'Id':i
#             }
#         )
fe = Key('Id').between(1, 11)
pe = 'Id'

response = table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe
)

print("get Item Succedded")
j= 0
for i in response['Items']:
    j+=1
    print(i)
    print(j,json.dumps(i, indent=4, cls=DecimalEncoder))