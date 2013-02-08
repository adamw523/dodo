import dodo.cfg

config = dodo.cfg.Config()

def connect(host=None, client_id=None, api_key=None):
    from dodo.connection import Connection
    return Connection(host, client_id, api_key)

