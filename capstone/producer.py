from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from kafka.client import SimpleClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer

TOPIC = "stonks"

SERVERS = ["localhost:9092","localhost:9093","localhost:9094"]


producer = KafkaProducer(bootstrap_servers=SERVERS)
consumer_key = "zRk1tHa1ONLXl8ERb7CVCNbCY"
consumer_secret = "iuRKQ3a3AqRJ7dU31K8AhnbTqVLjHBAkqmTaS2IR7vCcQMxYIB"
access_token = "1322200166179495942-KrUsTmHAaFFvMEjGFSKHDDIgPwpFZA"
access_token_secret = "gAgpuvnSq1HWqJ6Kbm37Lp1HstSvxZE3oha4aCvNwx9eV"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages(TOPIC, str(data))
        producer.flush()
        print(data)
        return True

    def on_error(self, status):
        print(status)


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['#aapl'],languages=["en"])