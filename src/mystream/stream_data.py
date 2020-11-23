import time
from google.cloud import pubsub_v1
from .tweets import get_tweets_stream
import os
import json


project = 'my-dataflow-project-296417'
pubsub_topic = 'projects/my-dataflow-project-296417/topics/tweets'
service_account_key = 'my-dataflow-project-296417-124ad71babe9.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key

publisher = pubsub_v1.PublisherClient()


def publish_to_topic():
	response = get_tweets_stream()
	counter = 0
	for response_line in response.iter_lines():
		if response_line:
			json_response = json.loads(response_line)
			row = json.dumps(json_response, indent=4, sort_keys=True)

			print(row)
			print(type(row))
			publisher.publish(pubsub_topic, row.encode("utf-8"))
			print("Publishing to the topic :" + row)
			counter = counter + 1
			time.sleep(1)

			if counter == 3:
				break


def main() -> None:
	print("Stream data main called!")
	publish_to_topic()


if __name__ == "__main__":
	main()
