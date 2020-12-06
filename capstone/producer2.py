from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
from kafka import KafkaClient


TOPIC = "stonks"

SERVERS = ["localhost:9092","localhost:9093","localhost:9094"]


consumer_key = "I2owvns6rDZpBXf7pMrox2KuI"
consumer_secret = "Deb5HvJp1yWpECKkCbD0KaRjiwmpSl8QzRblvvXWBeUXwlGnqM"
access_token = "1322200166179495942-I6MLoDWZ97WsuMNMGnwOjE1KHFeWGd"
access_token_secret = "OtB9zJfaaoPV45gT9oqu34mIVaseaCKpM8mlbPlewcRvA"
producer = KafkaProducer(bootstrap_servers=SERVERS)


class twitterAuth():
	def authenticateTwitterApp(self):
		auth = OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth



class TwitterStreamer():
	def __init__(self):
		self.twitterAuth = twitterAuth()
	def stream_tweets(self):
		while True:
			listener = ListenerTS()
			auth = self.twitterAuth.authenticateTwitterApp()
			stream = Stream(auth, listener)
			stream.filter(track=["MUFC"], stall_warnings=True, languages= ["en"])


class ListenerTS(StreamListener):
	def on_data(self, raw_data):
		producer.send(TOPIC, str.encode(raw_data))
		producer.flush()
		return True


if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()
