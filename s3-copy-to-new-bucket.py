#!/usr/bin/python3

###############################################################
## This code takes two buckets and transfers from objects    ##
## from one bucket to other bucket.                          ##
## It also copies ACLs and retains the object metadata.      ##
###############################################################

import boto3
from datetime import datetime

client = boto3.client('s3')
bucketOne = 'bucket1'
bucketTwo='bucket2'

kwargs={'Bucket':bucketOne}
listOfObjects=[]
failedObjects=[]
excludeObjects=[]
while True:
        response=client.list_objects_v2(**kwargs)
        for object in response['Contents']:
                generator_for_exclusions = (x in object['Key'] for x in excludeObjects)
                if any(generator_for_exclusions):
                        print("excluded --->" + object['Key'])
                else:
                        listOfObjects.append(object['Key'])
                        object_acl_response=client.get_object_acl(Bucket=bucketOne,Key=object['Key'])
                        object_acl={}
                        object_acl['Grants']=object_acl_response['Grants']
                        object_acl['Owner']=object_acl_response['Owner']
                        copy_response=client.copy_object(Bucket=bucketTwo,CopySource={'Bucket':bucketOne,'Key':object['Key']},Key=object['Key'],MetadataDirective='COPY')
                        if copy_response['ResponseMetadata']['HTTPStatusCode']!=200:
                                failedObjects.append(object['Key'])
                                print(str(datetime.now()) + "\t" +"ERROR: Copy Unsuccessful for Key: "+object['Key'])
                        else:
                                put_acl_response=client.put_object_acl(Bucket=bucketTwo,Key=object['Key'],AccessControlPolicy=object_acl)
                                if put_acl_response['ResponseMetadata']['HTTPStatusCode']!=200:
                                        print(str(datetime.now()) + "\t" +"ERROR: Copy ACL Unsuccessful for Key: "+object['Key'])
                                else:
                                        print(str(datetime.now()) + "\t" +"INFO: Copy Successful for Key: "+object['Key'])
        try:
                kwargs['ContinuationToken']=response['NextContinuationToken']
        except KeyError:
                break
print("Failed Objects: ")
for k in failedObjects:
        print(k)
