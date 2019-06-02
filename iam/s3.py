import boto3
import json
import pprint

session = boto3.Session(profile_name='master')
client = session.client('s3')

response = client.list_buckets()
pprint.pprint(response)

bucket_names = []
for bucket in response['Buckets']:
    bucket_names.append(bucket['Name'])
    print(bucket_names)

# Create a dictionary to hold the lists of object (file) names
bucket_objects = {}
# Loop through each bucket we found
for bucket in bucket_names:
    # Run our first API call to pull in the objects
    response = client.list_objects_v2(Bucket=bucket, MaxKeys=1000)
    # Check if there are any objects returned (none will return if no objects are in the bucket)
    if response.get('Contents'):
         # Store the fetched set of objects
         bucket_objects[bucket] = response['Contents']
    else:
        bucket_objects[bucket] = []
        continue
    
while response['IsTruncated']:
    response = client.list_objects_v2(Bucket=bucket, MaxKeys=1000,
    continuationToken=response['NextContinuationToken'])
    bucket_objects[bucket].extend(response['Contents'])

 # We know bucket_objects has a key for each bucket so let's iterate that

for bucket in bucket_names:
    # Open up a local file with the name of the bucket
    with open('./{}.txt'.format(bucket), 'w+') as f:
        # Iterate through each object in the bucket
        for bucket_object in bucket_objects[bucket]:
            # Write a line to our file with the object details we are
            # interested in (file name and size)
            f.write('{} ({} bytes)\n'.format(bucket_object['Key'],
   bucket_object['Size']))


