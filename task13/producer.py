from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer
from kafka import KafkaClient


access_token = 
token_secret = 
consumer_key = 
consumer_secret =
topic = "tweets"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(topic, data.encode('utf-8'))
        print ("Tweet Sent")
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, token_secret)
stream = Stream(auth, l)
stream.filter(track="Rashford")



