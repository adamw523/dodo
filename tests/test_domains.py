from dodo_test_case import DodoTestCase
from mock import MagicMock, Mock
from unittest import TestCase
import dodo
import requests

class DomainsTest(DodoTestCase):
    def test_get_domains(self):

        self.mock_get_json_asset('domains.json')

        res = self.conn.domains()

        requests.get.assert_called_with(self.host + '/domains/',
                headers=self.headers, params=self.params)

        assert len(res) == 1
        assert res[0]['name'] == "example.com"
        assert res[0]['ttl'] == 1800

