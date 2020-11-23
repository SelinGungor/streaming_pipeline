import requests
import os
import json

def create_headers(bearer_token):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	return headers


def set_rules(headers):
	# You can adjust the rules if needed
	sample_rules = [
		{"value": "corona lang:en", "tag": "corona"},
	]
	payload = {"add": sample_rules}
	response = requests.post(
		"https://api.twitter.com/2/tweets/search/stream/rules",
		headers=headers,
		json=payload,
	)
	if response.status_code != 201:
		raise Exception(
			"Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
		)
	print(json.dumps(response.json()))


def get_stream(headers):
	response = requests.get(
		"https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
	)
	print(response.status_code)
	if response.status_code != 200:
		raise Exception(
			"Cannot get stream (HTTP {}): {}".format(
				response.status_code, response.text
			)
		)
	for response_line in response.iter_lines():
		if response_line:
			json_response = json.loads(response_line)
			print(json.dumps(json_response, indent=4, sort_keys=True))


def get_headers():
	bearer_token = os.environ.get("BEARER_TOKEN")
	headers = create_headers(bearer_token)
	set = set_rules(headers)
	return bearer_token, headers, set


def get_tweets_stream():
	bearer_token, headers, set = get_headers()

	response = requests.get(
		"https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
	)
	print(response.status_code)
	if response.status_code != 200:
		raise Exception(
			"Cannot get stream (HTTP {}): {}".format(
				response.status_code, response.text
			)
		)

	return response


if __name__ == "__main__":
	get_tweets_stream()
