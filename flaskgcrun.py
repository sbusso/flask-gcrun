# template
from flask import Flask, request, g
import os
import time
import http
import logging
import json
import base64
from google.cloud import pubsub
from store import Store

# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)


class FlaskGCRun(Flask):
    channels = None

    def __init__(self, import_name, downstream_channels=[]):
        super(FlaskGCRun, self).__init__(import_name)
        self.PROJECT_ID = os.getenv('GCP_PROJECT')
        if os.getenv('BUCKET_NAME') != None:
            self._store = Store()
        self.downstream_channels = downstream_channels
        self.init_app()

    def init_app(self):
        self.before_request(self.before_request_func)
        self.teardown_request(self.teardown_request_func)
        self.route('/', methods=['POST'])(self.invoke)

    def decode(self, message):
        return json.loads(base64.b64decode(
            message['data']).decode('utf-8'), strict=False)

    def encode(self, message):
        return json.dumps(message).encode('utf-8')

    def invoke(self):
        envelope = request.get_json()

        if not envelope:
            msg = 'no Pub/Sub message received'
            logging.error(f'error: {msg}')
            return f'Bad Request: {msg}', 400

        if not isinstance(envelope, dict) or 'message' not in envelope:
            msg = 'invalid Pub/Sub message format'
            logging.error(f'error: {msg}', envelope)
            return f'Bad Request: {msg}', 400

        pubsub_message = envelope['message']

        data = self.decode(pubsub_message)
        response = self.handler(data)
        self.publish(response)
        return self.encode(response), http.HTTPStatus.OK

    def publish(self, message):
        if len(self.get_channels()) == 0:
            return
        data = self.encode(message)
        publisher = pubsub.PublisherClient()
        for channel in self.get_channels():
            path = publisher.topic_path(
                self.PROJECT_ID, channel)
            publish_future = publisher.publish(
                path, data=data)
            publish_future.result()

    # to be overridden
    def handler(self, data):
        return NotImplemented

    def store(self):
        if self._store != None:
            return self._store
        else:
            raise Exception("BUCKET NAME is not set")

    def before_request_func(self):
        g.start = time.time()

    def teardown_request_func(self, exception):
        diff = time.time() - g.start
        logging.info(f"time: {str(diff)}")

    def get_channels(self):
        if self.channels != None:
            return self.channels
        self.channels = []
        c = os.getenv('DOWNSTREAM_CHANNELS')
        if c != None:
            self.channels += c.split(',')
        self.channels += self.downstream_channels
        return self.channels
