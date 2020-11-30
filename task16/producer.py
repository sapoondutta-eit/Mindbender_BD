import requests
from kafka import SimpleProducer
from kafka import KafkaClient


TOPIC = "stockmarket"


url = "https://twelve-data1.p.rapidapi.com/rsi"

querystring = {"symbol":"FCEL","interval":"1min","series_type":"close","outputsize":"30","format":"json","time_period":"14"}

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

RSI = response.text

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)

producer.send_messages(TOPIC, RSI.encode('utf-8'))
