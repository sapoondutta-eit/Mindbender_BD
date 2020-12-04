import requests
from kafka import KafkaProducer
import time


TOPIC = "stockmarket"

SERVERS = ["localhost:9092","localhost:9093","localhost:9094"]

producer = KafkaProducer(bootstrap_servers=SERVERS)


url = "https://twelve-data1.p.rapidapi.com/quote"

symbol = ["AAPL","AMZN","FCEL","XSPA","PLTR","AUPH","ACB","TWTR","TSLA","NFLX","FB","MSFT","DIS"]



headers = {
    'x-rapidapi-key': "91c9731234mshaa0159144ccc387p15ba78jsn35630e0f0930",
    'x-rapidapi-host': "twelve-data1.p.rapidapi.com"
    }


a = 1
while(a > 0):
    for i in symbol: 
        time.sleep(10)
        querystring = {"symbol":i,"interval":"1day","format":"json","outputsize":"30"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        data = response.text

        producer.send(TOPIC,data.encode('utf-8'))
        producer.flush()
    a = a - 1


