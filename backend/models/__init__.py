import json
from mongoengine import Document


class SerializableModel(Document):
    """
    A Document model that can be serializable to JSON with the option
    to ignore specific fields.
    """
    meta = {"allow_inheritance" : True}

    IGNORE_FIELDS = []

    def to_json(self):
        json_data = super(SerializableModel, self).to_json()
        parsed_json = json.loads(json_data)
        for field in self.__class__.IGNORE_FIELDS:
            del parsed_json[field]

        return json.dumps(parsed_json)
