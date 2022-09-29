import json

import jsonpath


class Post:
    def __init__(self, data):
        self.data = data

    def get_status_code(self):
        return self.data.status_code

    def verify_properties(self, key):
        return jsonpath.jsonpath(json.loads(self.data.text), key)

    def reason(self):
        return self.data.reason

    def content_type(self):
        return self.data.headers.get("Content-Type")
