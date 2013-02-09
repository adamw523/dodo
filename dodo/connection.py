#######################################################################
# Copyright (c) 2013 Adam Wisniewski, http://adamw523.com
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import dodo
import requests

class Connection:
    def __init__(self, host=None, client_id=None, api_key=None):
        config = dodo.config

        self.host = host or config.host
        self.client_id = client_id or config.client_id
        self.api_key = api_key or config.api_key

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

    def new_droplet(self, name, size_id, image_id, region_id, ssh_key_ids):
        path = 'droplets/new'
        res = self.get_json(path, {'size_id': size_id, 'image_id': image_id,
            'region_id': region_id, 'ssh_key_ids': ssh_key_ids, 'name': name})
        return res

    def destroy_droplet(self, droplet_id):
        path = 'droplets/%(droplet_id)s/destroy'
        res = self.get_json(path, {}, {'droplet_id': droplet_id})
        return res

    def show_droplet(self, droplet_id):
        path = 'droplets/%(droplet_id)s'
        res = self.get_json(path, {}, {'droplet_id': droplet_id})
        return res['droplet']

    # Images
    def images(self, ifilter=None):
        path = 'images/'
        if ifilter:
            res = self.get_json(path, {'filter': ifilter})
        else:
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



