# Flask Google Run

This module provides the base elements to create a service with Flask and run on Google Run, it also includes a client to publish messages to a pubsub topic.

## Usage

The minimum code to run a service:

```python
from flaskgcrun import FlaskGCRun

class Service(FlaskGCRun):
    def handler(self, data):
        return data

app = Service(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', 
            port=int(os.environ.get('PORT', 8080)))
```

`handler` is the required method to process _data_.

`FlaskGCRun` class provides utilities:

- store
- logging
- pub/sub publisher

it's automatically handle decoding of messages and log excecution time.

The service will forward _data_ returned by `handler` to downstream queues, if _data_ is not `None` and if a list of downstream channels is provided either in the class constructor or with the `DOWNSTREAM_CHANNELS` environment variable.

### Store utility

Store utility provides 3 methods to upload or retireive files:

- upload_string
- upload_blob
- list_blobs

## TODO

- [X] to disable pubsub
- [ ] to return always OK
- [ ] use ENV for everything + default