import re
import tweepy
#import mysql.connector
import pandas as pd
from textblob import TextBlob
from kafka import KafkaProducer
from kafka import KafkaClient
import json
# Streaming With Tweepy 
# http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html#streaming-with-tweepy
TOPIC = "stonks"

SERVERS = ["localhost:9092","localhost:9093","localhost:9094"]

producer = KafkaProducer(bootstrap_servers=SERVERS)

# Override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \ |(\w+:\/\/\S+)", " ", tweet).split()) 

    def deEmojify(self,text):
        if text:
            return text.encode('ascii', 'ignore').decode('ascii')
        else:
            return None


    def on_status(self, status):

        if status.retweeted:
            return True

        id_str = status.id_str
        created_at = status.created_at
        text = self.deEmojify(status.text)    # Pre-processing the text  
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        
        user_created_at = status.user.created_at
        user_location = self.deEmojify(status.user.location)
        user_description = self.deEmojify(status.user.description)
        user_followers_count =status.user.followers_count
        longitude = None
        latitude = None
        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]
            
        retweet_count = status.retweet_count
        favorite_count = status.favorite_count



        data = (status.id,text,polarity,subjectivity)
        # print(data)

        # for a in data:
        #     print(a)

        # #print(data)
        # #print(status.id, "  ",text, "  ", polarity,"   ", subjectivity)
        producer.send(TOPIC, json.dumps(data).encode('utf-8'))
        producer.flush()

        #print("Long: {}, Lati: {}".format(longitude, latitude))
        
        # Store all data in MySQL
        # if mydb.is_connected():
        #     mycursor = mydb.cursor()
        #     sql = "INSERT INTO {} (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(settings.TABLE_NAME)
        #     val = (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, \
        #         user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count)
        #     mycursor.execute(sql, val)
        #     mydb.commit()
        #     mycursor.close()
    

    

#MyStreamListener = MyStreamListener()

auth  = tweepy.OAuthHandler("I2owvns6rDZpBXf7pMrox2KuI", "Deb5HvJp1yWpECKkCbD0KaRjiwmpSl8QzRblvvXWBeUXwlGnqM")
auth.set_access_token("1322200166179495942-BhG01AM8BARPfk6I4dVbnIelMAu4aS", "VHnX2IpGBYv9agYkanfE2MmAgwDvSCX4A7LHcSJLh2iak")
api = tweepy.API(auth)
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
data = myStream.filter(languages=["en"], track = ["PLTR","Palantir"])
