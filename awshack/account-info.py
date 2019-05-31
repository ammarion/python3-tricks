import boto3
import json
session = boto3.Session(profile_name='master', region_name='us-east-1')

client = session.client('iam')
# Declare the variables that will store the enumerated information
user_details = []
group_details = []
role_details = []
policy_details = []

 # Make our first get_account_authorization_details API call

response = client.get_account_authorization_details()

# Store this first set of data
if response.get('UserDetailList'):
    user_details.extend(response['UserDetailList'])

if response.get('GroupDetailList'):
    group_details.extend(response['GroupDetailList'])

if response.get('RoleDetailList'):
    role_details.extend(response['RoleDetailList'])

if response.get('Policies'):
    policy_details.extend(response['Policies'])

 # Check to see if there is more data to grab
while response['IsTruncated']:
    # Make the request for the next page of details
    # response =
    client.get_account_authorization_details(Marker=response['Marker'])
# Store the data again
    if response.get('UserDetailList'):
        user_details.extend(response['UserDetailList'])
    if response.get('GroupDetailList'):
        group_details.extend(response['GroupDetailList'])
    if response.get('RoleDetailList'):
        role_details.extend(response['Policies'])

# Open up each file and dump the respective JSON into them

with open('./users.json', 'w+') as f:
    json.dump(user_details, f, indent=4, default=str)

with open('./groups.json', 'w+') as f:
    json.dump(group_details, f, indent=4, default=str)

with open('./roles.json', 'w+') as f:
    json.dump(role_details, f, indent=4, default=str)

with open('./policies.json', 'w+') as f:
    json.dump(policy_details, f, indent=4, default=str)

username = client.get_user()['User']['UserName']
# Define a variable that will hold our user
current_user = None

# Iterate through the enumerated users
for user in user_details:
    # See if this user is our user
    if user['UserName'] == username:
        # Set the current_user variable to our user
        current_user = user

        # We found the user, so we don't need to iterate through the rest of them
        break
# Create an empty list that will hold all the policies related to our user 
my_policies = []
# Check if any inline policies are attached to my user
if current_user.get('UserPolicyList'):
    # Iterate through the inline policies to pull their documents
    for policy in current_user['UserPolicyList']:
        # Add the policy to our list
        my_policies.append(policy['PolicyDocument'])

# Check if any managed policies are attached to my user
if current_user.get('AttachedManagedPolicies'):
    # Iterate through the list of managed policies
    for managed_policy in user['AttachedManagedPolicies']:
        policy_arn = managed_policy['PolicyArn']

        # Iterate through the policies stored in policy_details to find this policy
