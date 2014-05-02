from dodo_test_case import DodoTestCase
from mock import MagicMock, Mock
from unittest import TestCase
import dodo
import requests

class DodoTest(DodoTestCase):

    def test_show_event(self):
        self.mock_get_json_asset('event.json')
        res = self.conn.show_event('7499')

        requests.get.assert_called_with(self.host + '/events/7499',
                headers=self.headers, params=self.params)

        assert res['id'] == 7499
        assert res['action_status'] == 'done'

