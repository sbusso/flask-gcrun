from google.cloud import storage
import os


class Store(object):
    def __init__(self):
        self._store = storage.Client()
        self.BUCKET_NAME = os.getenv('BUCKET_NAME')
        self._bucket = self._store.get_bucket(self.BUCKET_NAME)

    def upload_string(self, s, filename):
        blob = self._bucket.blob(filename)
        blob.upload_from_string(s)

    def upload_blob(self, source, filename):
        blob = self._bucket.blob(filename)
        blob.upload_from_filename(source)

    def list_blobs(self, prefix):
        return self._bucket.list_blobs(prefix=prefix)
