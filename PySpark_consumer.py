import os

os.environ[
    "PYSPARK_SUBMIT_ARGS"
] = "--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,org.elasticsearch:elasticsearch-spark-30_2.12:7.14.2 pyspark-shell"

import json

import math

from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import from_json, col
from pyspark import SparkContext

from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from subprocess import check_output

es = Elasticsearch(hosts=['localhost'], port=9200)

topic = "flight-realtime"
ETH0_IP = check_output(["hostname"]).decode(encoding="utf-8").strip()

SPARK_MASTER_URL = "local[*]"
SPARK_DRIVER_HOST = ETH0_IP

spark_conf = SparkConf()
spark_conf.setAll(
    [
        ("spark.master", SPARK_MASTER_URL),
        ("spark.driver.bindAddress", "0.0.0.0"),
        ("spark.driver.host", SPARK_DRIVER_HOST),
        ("spark.app.name", "Flight-infos"),
        ("spark.submit.deployMode", "client"),
        ("spark.ui.showConsoleProgress", "true"),
        ("spark.eventLog.enabled", "false"),
        ("spark.logConf", "false"),
    ]
)

def getrows(df, rownums=None):
    return df.rdd.zipWithIndex().filter(lambda x: x[1] in rownums).map(lambda x: x[0])

if __name__ == "__main__":
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")
        .option("subscribe", "flight-realtime")
        .option("enable.auto.commit", "true")
        .load()
    )
    def func_call(df, batch_id):
        df.selectExpr("CAST(value AS STRING) as json")
        requests = df.rdd.map(lambda x: x.value).collect()
        flight = getrows(df,rownums=[0]).collect()
        for i in flight:
           #print(i)
           print(i[1].decode("utf-8"))
           hex = i[1].decode("utf-8")
           #print(hex[9:15])
           dictio = eval(hex)
           print(type(dictio))
      
           print("writing_to_Elasticsearch")
           es.index(
                    index="flight-realtime-project",
                    doc_type="test_doc",
                    body={
		            "hex": dictio["hex"],
		            "reg_number": dictio["reg_number"],
		            "flag": dictio["flag"],
		            "lat": dictio["lat"],
		            "lng": dictio["lng"],
		            "alt": dictio["alt"],
		            "dir": dictio["dir"],
		            "speed": dictio["speed"],
		            "flight_number": dictio["flight_number"],
		            "flight_icao": dictio["flight_icao"],
		            "flight_iata": dictio["flight_iata"],
		            "dep_icao": dictio["dep_icao"],
		            "dep_iata": dictio["dep_iata"],
		            "arr_icao": dictio["arr_icao"],
		            "arr_iata": dictio["arr_iata"],
		            "airline_icao": dictio["airline_icao"],
		            "airline_iata": dictio["airline_iata"],
		            "aircraft_icao": dictio["aircraft_icao"],
		            "updated": dictio["updated"],
		            "status": dictio["status"]
                    
                    
                    }
                )

           
    query = df.writeStream \
    .format('console') \
    .foreachBatch(func_call) \
    .trigger(processingTime="30 seconds") \
    .start().awaitTermination()


  
