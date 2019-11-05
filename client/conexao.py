
class Ip:
    def __init__(self):
        self._addr_server = (('localhost', 7000))

    @property
    def addr_server(self):
        return self._addr_server