# Subscribe to the queue

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions, SetupOptions
import os
# from apache_beam import window

project = 'my-dataflow-project-296417'
pubsub_topic = 'projects/my-dataflow-project-296417/topics/tweets'
output_topic='projects/my-dataflow-project-296417/topics/output-topic-tweets'
service_account_key = '*'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_key

input_subscription = "projects/my-dataflow-project-296417/subscriptions/tweets_subscription"

import argparse

def run(arguments=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--output_topic',
        required=False,
        help=('Output PubSub topic'), default=output_topic)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        '--input_topic',
        help=(
            'Input PubSub topic.'), default=pubsub_topic)
    group.add_argument(
        '--input_subscription',
        help=(
            'Input PubSub subscription'), default=input_subscription)

    known_args, pipeline_args = parser.parse_known_args(arguments)

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    pipeline_options.view_as(StandardOptions).streaming = True


    with beam.Pipeline(options=pipeline_options) as p:
        (p
              | 'ReadData' >> beam.io.ReadFromPubSub(subscription=input_subscription).with_output_types(bytes)
              | "Decode" >> beam.Map(lambda x: x.decode('utf-8'))
              | 'WriteToBigQuery' >> beam.io.WriteToBigQuery('{0}:tweets_dataset.output'.format(project),
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
           )
    result = p.run()
    result.wait_until_finish()



if __name__ == '__main__':
  run()
