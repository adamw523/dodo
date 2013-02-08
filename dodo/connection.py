import dodo
import requests

class Connection:
    def __init__(self, host=None, client_id=None, api_key=None):
        config = dodo.config

        self.host = host or config.host
        self.client_id = client_id or config.client_id
        self.api_key = api_key or config.api_key

        print dodo.config, 'test'

    ##############################
    # Helper functions

    def build_params(self, in_params):
        params = {  'client_id': self.client_id,
                    'api_key': self.api_key }
        params.update(in_params)
        return params

    def get(self, path, params={}, path_params={}):
        # build path
        path = path % path_params

        # build params with standard params + input
        params = self.build_params(params)

        url = self.host + '/' + path
        r = requests.get(url, params=params)
        return r

    def get_json(self, path, params={}, path_params={}):
        r = self.get(path, params, path_params)
        return r.json()

    ##############################
    # API Calls

    # Droplets
    def droplets(self):
        path = 'droplets/'
        res = self.get_json(path)
        return res['droplets']

    def new_droplet(self, size_id, image_id, region_id, ssh_key_ids):
        path = 'droplets/new'
        res = self.get_json(path)
        return res['droplets']

    # Images
    def images(self):
        path = 'images/'
        res = self.get_json(path)
        return res['images']

    # Regions
    def regions(self):
        path = 'regions/'
        res = self.get_json(path)
        return res['regions']

    # Sizes
    def sizes(self):
        path = 'sizes/'
        res = self.get_json(path)
        return res['sizes']

    # SSH Keys
    def ssh_keys(self):
        path = 'ssh_keys/'
        res = self.get_json(path)
        return res['ssh_keys']

    def ssh_key(self, ssh_key_id):
        path = 'ssh_keys/%(ssh_key_id)s/'
        res = self.get_json(path, {}, {'ssh_key_id': ssh_key_id})
        #if res['ssh_key
        return res['ssh_key']

    # TODO: add not implemented yet
    def add_ssh_key(self, ssh_key_name, ssh_key_pub):
        path = 'ssh_key/%(ssh_key_id)/add/'
        res = self.get_json(path, {'ssh_key_name': ssh_key_name,
            'ssh_key_pub': ssh_key_pub})
        return res



