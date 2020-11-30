import requests
from kafka import SimpleProducer
from kafka import KafkaClient

TOPIC = "footballapi"

url = "https://api-football-v1.p.rapidapi.com/v2/topscorers/2"

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

text = response.text

kafka = KafkaClient("localhost:9099")
producer = SimpleProducer(kafka)

producer.send_messages(TOPIC, text.encode('utf-8'))
