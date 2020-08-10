import unittest
from unittest import mock
from flaskgcrun import FlaskGCRun
import json
import os
import base64


class TestFlaskGCRunClass(FlaskGCRun):
    def handler(self, data):
        return data


class TestFlaskGCRun(unittest.TestCase):
    def setUp(self):
        self.server = TestFlaskGCRunClass(__name__)
        self.server.config['TESTING'] = True
        self.app = self.server.test_client()

    def test_get_channels(self):
        self.server_channel = FlaskGCRun('The server', ['hello'])
        k = mock.patch.dict(os.environ, {"DOWNSTREAM_CHANNELS": "one,two"})
        k.start()
        self.assertListEqual(self.server_channel.get_channels(), [
            'one', 'two', 'hello'], "Should be set")
        k.stop()

    def test_routes(self):
        with self.app as c:
            response = c.post('/')
            self.assertEqual(response.status_code, 400)
            s = json.dumps(
                {"output": "test"})
            message = base64.b64encode(s.encode('utf-8')).decode('ascii')
            response = c.post(
                '/', data=json.dumps({"message": {"data": message}}), content_type='application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
