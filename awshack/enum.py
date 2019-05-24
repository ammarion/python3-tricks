#!/usr/bin/env python3
import boto3
import pprint
import json
session = boto3.Session(profile_name='master', region_name='us-east-1')

client = session.client('ec2')

 # First, create an empty list for the enumerated instances to be stored in
instances = []

''' 
  Next, make our initial API call with MaxResults set to 1000, 
  which is the max
  This will ensure we are making as few API calls as possible
'''

response = client.describe_instances(MaxResults=1000)
pprint.pprint(response)

# The top level of the results will be "Reservations" so iterate through those

for reservation in response['Reservations']:
    # Check if any instances are in this reservation
    if reservation.get('Instances'):
        # Merge the list of instances into the list we created earlier
        instances.extend(reservation['Instances'])
        print(len(instances))
        pprint.pprint(instances[0])
'''
 esponse['NextToken'] will be a valid value 
 if we don't have all the results yet.
 It will be "None" if we have completed enumeration of the instances
 So we need check if it has a valid value, 
 and because this could happen again, we will need to make it a loop
# As long as NextToken has a valid value, do the following, otherwise skip
   it
'''
while response.get('NextToken'):
    # Run the API call again while supplying the previous calls NextToken
    # This will get us the next page of 1000 results
    response = client.describe_instances(MaxResults=1000,
     NextToken=response['NextToken'])
'''
Iterate the reservations and add any instances found to our variable
again
'''
for reservation in response['Reservations']:
    if reservation.get('Instances'):
        instances.extend(reservation['Instances'])

'''
Open up the local file we are going to store our data in
'''
with open('./ec2-instances.json', 'w+') as f:
    '''
    Use the json library to dump the contents to the newly opened file
   with some indentation to make it easier to read. Default=str to convert
   dates to strings prior to dumping, so there are no errors
    '''
    json.dump(instances, f, indent=4, default=str)


s3_client = session.client('s3')