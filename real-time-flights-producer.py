import json
import time

import urllib.request
from urllib.request import Request, urlopen

from kafka import KafkaProducer

API_KEY = "dc019782-c207-4c85-85d3-bb4d4e1d0845"

url = "https://airlabs.co/api/v9/flights?api_key={}".format(API_KEY)

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:

 response = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0'})
 flights = json.loads(urlopen(response).read().decode())

 for flight in flights["response"]:

   print(flight)

   producer.send("flight-realtime", json.dumps(flight).encode())

 print("{} Produced {} station records".format(time.time(), len(flights)))

 time.sleep(1)
