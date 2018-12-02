import boto3

ec2 = boto3.resource('ec2')

# instance = ec2.create_instances(
#     ImageId='ami-0f65671a86f061fcd',
#     MinCount=1,
#     MaxCount=1,
#     InstanceType='t2.micro'
# )


# print(instance[0].id)

instance_id='i-0dc7552c44f375d82'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)
