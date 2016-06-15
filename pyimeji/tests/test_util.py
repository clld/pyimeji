import os

from unittest import TestCase
from pyimeji.api import Imeji


class Tests(TestCase):
    def test_jsonload(self):
        from pyimeji.util import jsonload

        self.assertEquals(
            jsonload(os.path.join(os.path.dirname(__file__), 'test.json'))['status'],
            'ok')


    def test_jsondumps(self):
        from pyimeji.util import jsondumps
        api = Imeji()
        default_profile = api.profile("default")
        collection = api.create('collection', title="TEST DUMPER",
                                         profile={'id': default_profile._json["id"], 'method': 'reference'})
        json_collection = collection.dumps()
        self.assertTrue('TEST DUMPER' in json_collection)
        collection.delete()
