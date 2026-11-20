import json
import traceback

from .api_adaptee import ApiAdaptee
from .target import Record, Target


class ApiAdapter(Target[Record]):

    def __init__(self, api_adaptee: ApiAdaptee[str]) -> None:
        self._api_adaptee = api_adaptee

    def fetch_data(self) -> Record:
        json_string = self._api_adaptee()

        try:
            json_object = json.loads(json_string)
            return Record(json_object["id"], json_object["name"])
        except Exception:
            # todo log error
            traceback.print_exc()

        return Record(None, None)
