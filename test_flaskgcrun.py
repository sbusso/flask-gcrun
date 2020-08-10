import unittest
from unittest import mock
from flaskgcrun import FlaskGCRun

import os


class TestFlaskGCRun(unittest.TestCase):
    def setUp(self):
        self.server = FlaskGCRun('The server', ['hello'])

    def test_get_channels(self):
        k = mock.patch.dict(os.environ, {"DOWNSTREAM_CHANNELS": "one,two"})
        k.start()
        self.assertListEqual(self.server.get_channels(), [
            'one', 'two', 'hello'], "Should be set")
        k.stop()


if __name__ == '__main__':
    unittest.main()
