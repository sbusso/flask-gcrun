from google.cloud import storage
import os


class Store(object):
    def __init__(self) -> None:
        self.store = storage.Client()
        self.BUCKET_NAME = os.getenv('BUCKET_NAME')
        self.bucket = self.store.get_bucket(self.BUCKET_NAME)

    def upload_string(self, s, filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_string(s)

    def upload_blob(self, source, filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_filename(source)

    def list_blobs(self, prefix):
        self.bucket.list_blobs(prefix=prefix)