# template
from flask import Flask, request, g
import os
import time
import http
import logging
import json


# Change the format of messages logged to Stackdriver
logging.basicConfig(format='%(message)s', level=logging.INFO)


class FlaskGCRun(Flask):
    def __init__(self, import_name, downstream_channels=[]):
        super(FlaskGCRun, self).__init__(import_name)
        self.PROJECT_ID = os.getenv('PROJECT_ID')
        self.downstream_channels = downstream_channels
        self.init_app()

    def init_app(self):
        self.before_request(self.before_request_func)
        self.after_request(self.after_request_func)
        self.teardown_request(self.teardown_request_func)
        self.client = {}
        self.route('/', methods=['POST'])(self.invoke)

    def decode(self, message):
        return {"project_id": self.PROJECT_ID}

    def encode(self, resp):
        return ""

    def invoke(self):
        data = self.decode(request)
        response = self.handler(data)
        # self.client.process(response)
        self.publish()
        # return self.encode(response), http.HTTPStatus.OK
        return response, http.HTTPStatus.OK

    def publish(self):
        pass
    # to be overridden

    def handler(self, data):
        return NotImplemented

    def before_request_func(self):
        g.start = time.time()

    def after_request_func(self, response):
        diff = time.time() - g.start
        if ((response.response) and
                (200 <= response.status_code < 300)):
            d = json.loads(response.get_data())
            d['time'] = str(diff)
            response.set_data(json.dumps(d))

        return response

    def teardown_request_func(self, exception):
        diff = time.time() - g.start
        logging.info(f"time: {str(diff)}")

# def create_app():
#     app = Flask(__name__)

#     return app
