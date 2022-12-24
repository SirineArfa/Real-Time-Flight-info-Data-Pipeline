# Creating a Real-Time Flight-info Data Pipeline with Kafka, Apache Spark, Elasticsearch and Kibana

In this project, we will use a real-time flight tracking API, Apache Kafka, ElastichSearch and Kibana to create a real-time Flight-info data pipeline and track the flights in real-time. We will use a high-level architecture and
corresponding configurations that will allow us to create this data pipeline. The end result will be a Kibana dashboard fetching real-time data from ElasticSearch.

![a](https://user-images.githubusercontent.com/80635318/209438803-10e11a67-12c4-4dca-9a13-eeef20a1f8ce.PNG)

![b](https://user-images.githubusercontent.com/80635318/209438806-ba08a62c-046c-4576-ad5b-322a34d57442.PNG)

![c](https://user-images.githubusercontent.com/80635318/209438812-508ad5b4-0df6-492a-8f36-90bc5af0013c.PNG)


## Pipeline
Our project pipeline is as follows:

![2](https://user-images.githubusercontent.com/80635318/209438588-6f71c44e-c24f-4e80-b8bd-e3168f9bf963.PNG)

## Prerequisites
The following software should be installed on your machine in order to reproduice our work:

- Spark (spark-3.3.1-bin-hadoop2.7)
- Kafka (kafka_2.13-2.7.0)
- ElasticSearch (elasticsearch-7.14.2)
- Kibana (kibana-7.14.2)
- Python 3.9.6
## Steps
###### Get Flight API:
We started by collecting in real-time Flight informations (Aircraft Registration Number,Aircraft Geo-Latitude,Aircraft Geo-Longitude,Aircraft elevation,Flight numbe...) and then we sent them to Kafka for analytics.

###### Kafka Real-Time Producer:
The data is ingested from the flight streaming data API and sent to a kafka topic. You need to run Kafka Server with Zookeeper and create a dedicated topic for data transport.
###### PySpark Streaming:
 In Spark Streaming, Kafka consumer is created that periodically collect data in real time from the kafka topic and send them into an Elasticsearch index.
###### Index flight-info to Elasticsearch:
You need to enable and start Elasticsearch and run it to store the flight-info and their realtime information for further visualization purpose. You can navigate to http://localhost:9200 to check if it's up and running.
###### Kibana for visualization
Kibana is a visualization tool that can explore the data stored in elasticsearch. In our project, instead of directly output the result, we used this visualization tool to visualize the streaming data in a real-time manner.You can navigate to http://localhost:5601 to check if it's up and running.

## How to run
1. Start Elasticsearch

`sudo systemctl start elasticsearch ` & `sudo systemctl enable elasticsearch `

2. Start Kibana

`sudo systemctl start kibana ` & `sudo systemctl enable kibana  `

3. Start Zookeeper server by moving into the bin folder of Zookeeper installed directory by using:

`./bin/zookeeper-server-start.sh ./config/zookeeper.properties`

4. Start Kafka server by moving into the bin folder of Kafka installed directory by using:

`./bin/kafka-server-start.sh ./config/server.properties`

5. Run Kafka producer:

`python3 ./real-time-flights-producer.py`

6. Run PySpark consumer with spark-submit:

`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,,org.elasticsearch:elasticsearch-spark-30_2.12:7.14.2 /home/sirine/Downloads/spark_consumer.py`





