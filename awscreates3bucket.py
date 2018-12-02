import boto3

s3 = boto3.resource('s3')
# s3= boto3.client('s3')
bucketname='bbbbuket'
try:
    # response = s3.create_bucket(Bucket=bucketname, CreateBucketConfiguration={'LocationConstraint':'us-east-2'} )
    # print(response)
    ## uploading file to s3 bucket
    # s3.upload_file('C:\\Users\\Sam\\Documents\\python\\pythonTutorial\\PythonImageProcessing\\Chapter-07\\knn.py',bucketname,'upladedfile.txt')
    ## Download file
    s3.Bucket(bucketname).download_file('upladedfile.txt', 'C:\\Users\\Sam\\Documents\\python\\pythonTutorial\\PythonImageProcessing\\Chapter-07\\myuploadedfile.py')




except Exception as err:
    print(err)

# try:
#     bucket = s3.Bucket(bucketname)
#     reponse =bucket.delete()
#     print(reponse)
# except Exception as err:
#     print(err)