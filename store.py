from google.cloud import storage


class Store(object):
    client = None

    def __init__(self, bucket_name):
        Store.client = storage.Client()
        self.BUCKET_NAME = bucket_name
        self._bucket = Store.client.get_bucket(self.BUCKET_NAME)

    def upload_string(self, s, filename):
        blob = self._bucket.blob(filename)
        blob.upload_from_string(s)

    def upload_blob(self, source, filename):
        blob = self._bucket.blob(filename)
        blob.upload_from_filename(source)

    def delete_directory(self, prefix):
        blobs = self.list_blobs(prefix)
        for blob in blobs:
            blob.delete()

    def list_blobs(self, prefix):
        return self._bucket.list_blobs(prefix=prefix)
