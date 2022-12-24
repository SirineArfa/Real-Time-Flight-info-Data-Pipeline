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
## Steps
######## 1.Flight API:
We started by collecting in real-time Flight informations (Aircraft Registration Number,Aircraft Geo-Latitude,Aircraft Geo-Longitude,Aircraft elevation,Flight numbe...) and then we sent them to Kafka for analytics.

######## 2.Flight API:
