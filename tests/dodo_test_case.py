from mock import MagicMock, Mock
from unittest import TestCase
import dodo
import json
import os
import requests

class DodoTestCase(TestCase):
    def setUp(self):
        self.host = 'http://test.example.com'
        self.client_id = 'fake_client'
        self.api_key = 'fake_key'
        self.headers = {'User-Agent': dodo.USER_AGENT}
        self.params = {'api_key': self.api_key, 'client_id': self.client_id}

        self.conn = dodo.connect(self.host, self.client_id, self.api_key)

    def asset_path(self, asset_file):
        """Return path to asset file relative to tests directory"""
        return os.path.join(os.path.dirname(__file__), 'assets', asset_file)

    def mock_get_json_asset(self, asset_file):
        """Mock requests.get result.json with contents of asset_file"""
        get_mock = Mock()

        with open(self.asset_path(asset_file), 'r') as f:
            get_mock.json = Mock(return_value=json.load(f))

        requests.get = Mock(return_value=get_mock)
