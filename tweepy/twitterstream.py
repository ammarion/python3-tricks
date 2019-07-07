from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import boto3
import os

# Session
session = boto3.Session(profile_name='nordstrom-federated')

# DynamoDB table name and Region
dynamoDBTable=os.environ['DYNAMODBTABLE']
region_name=os.environ['AWSREGION']

# Filter variable (the word for which to filter in your stream)
filter=os.environ['FILTER']

consumer_key=os.environ['CONSUMERKEY']
consumer_secret=os.environ['CONSUMERSECRETKEY']

# OkWvZewDdWyLjoc9rhBAiV0mO  (API key)
# 91O2E0VhoHQJ4lgJWRlMLCF7beXFhUaAnZnGJdnc8Kqtwyq4As (API secret key)


# After the step above, you are redirected to your app page.
# Create an access token under the "Your access token" section
access_token=os.environ['ACCESSTOKEN']
access_token_secret=os.environ['ACCESSTOKENSECRET']

# 896876624490237954-WyV8GIZnfO1jDSVUMIqQJxx7IeSDEM2 (Access token)
# xVVUrp82oxP4Xe0PWlfZRrxT9g2bWyhVuSI518tXQTzPN (Access token secret)

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that prints received tweets to stdout.
    """
    def on_data(self, data):
        j = json.loads(data)
        tweetuser = j['user']['screen_name']
        tweetdate = j['created_at']
        tweettext = j['text'].encode('ascii', 'ignore').decode('ascii')
        print(tweetuser)
        print(tweetdate)
        print(tweettext)
        dynamodb = boto3.client('dynamodb',region_name)
        dynamodb.put_item(TableName=dynamoDBTable, Item={'user':{'S':tweetuser},'date':{'S':tweetdate},'text':{'S':tweettext}})
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
stream.filter(track=[filter])