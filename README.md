# Streaming pipeline

This project gets the data from Twitter Streaming API and publishes the "Corona" related tweets to Google Cloud Pub/Sub.
After the tweets are published the Apache Beam processes the data and saves the results to BigQuery.


# Installation

```bash
cd my_streaming_pipeline/
conda create python=3.7 -p venv/ -y
conda activate venv/
pip install -e .
pip install -r requirements.txt
pip install "apache-beam[gcp]"
```

# Running the project

## Publish the tweets to GCP Pub/Sub

1. Get the BEARER_TOKEN from Twitter application
1. Create a GCP project
1. Create a GCP pub/sub topic

```bash
export BEARER_TOKEN=""
mystream
```

## Consume the tweets and save them to BigQuery

1. Create a GCP Subscriber 
1. Create a BigQuery Dataset, table

```bash
python src/mystream/subscriber.py
```