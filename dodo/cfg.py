from ConfigParser import SafeConfigParser
import os.path

class Config:
    def __init__(self, host='https://api.digitalocean.com'):

        # get the paths that we might want to use
        paths = [os.path.expanduser('~/.dodo')]

        # get parser
        self.parser = SafeConfigParser()
        self.parser.read(paths)

        # set config options
        self.host = host
        self.client_id = self.parser.get('credentials', 'client')
        self.api_key = self.parser.get('credentials', 'api')




