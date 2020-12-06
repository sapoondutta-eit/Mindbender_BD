#!/usr/bin/env python


# import required libraries
from kafka import KafkaProducer, KafkaClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from afinn import Afinn

# Kafka settings
topic = "stonks"

# setting up Kafka producer
SERVERS = ["localhost:9092","localhost:9093","localhost:9094"]
producer = KafkaProducer(bootstrap_servers=SERVERS)

####keys 
consumer_key = "I2owvns6rDZpBXf7pMrox2KuI"
consumer_secret = "Deb5HvJp1yWpECKkCbD0KaRjiwmpSl8QzRblvvXWBeUXwlGnqM"
access_token = "1322200166179495942-I6MLoDWZ97WsuMNMGnwOjE1KHFeWGd"
access_token_secret = "OtB9zJfaaoPV45gT9oqu34mIVaseaCKpM8mlbPlewcRvA"


#This is a basic listener that just put received tweets to kafka cluster.
class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(topic, data.encode('utf-8'))
        #print data
        return True

    def on_error(self, status):
        print(status)

WORDS_TO_TRACK = "AAPL FCEL PLTR TRUMP".split()

if __name__ == '__main__':
    print( 'running the twitter-stream python code')
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    afinn = Afinn()
    # Goal is to keep this process always going
    while True:
        try:
           # stream.sample()
            stream.filter(languages=["en"], track=WORDS_TO_TRACK)
        except:
            pass
