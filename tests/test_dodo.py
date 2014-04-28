from mock import MagicMock, Mock
from unittest import TestCase
import dodo
import requests

class DodoTest(TestCase):
    def setUp(self):
        self.host = 'http://test.example.com'
        self.client_id = 'fake_client'
        self.api_key = 'fake_key'
        self.headers = {'User-Agent': dodo.USER_AGENT}
        self.params = {'api_key': self.api_key, 'client_id': self.client_id}

        self.conn = dodo.connect(self.host, self.client_id, self.api_key)

    def tearDown(self):
        pass

    def mock_get_json(self, json):
        get_mock = Mock()
        get_mock.json = Mock(return_value = json)
        requests.get = Mock(return_value=get_mock)

    def test_show_event(self):
        self.mock_get_json({'status': 'OK', 'event':
            {'event_type_id': 10, 'percentage': '100',
                'droplet_id': 1504592, 'id': 22439120,
                'action_status': 'done'}})

        res = self.conn.show_event('1234')

        requests.get.assert_called_with(self.host + '/events/1234',
                headers=self.headers, params=self.params)
        assert res['action_status'] == 'done'


