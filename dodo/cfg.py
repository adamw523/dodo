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

from ConfigParser import SafeConfigParser
import os.path

class Config:
    def __init__(self, host='https://api.digitalocean.com'):

        # get the paths that we might want to use
        paths = [os.path.expanduser('~/.dodo')]

        if os.path.exists(paths[0]):
            # get parser
            self.parser = SafeConfigParser()
            self.parser.read(paths)

            # set config options
            self.host = host
            self.client_id = self.parser.get('credentials', 'client')
            self.api_key = self.parser.get('credentials', 'api')
        else:
            pass




