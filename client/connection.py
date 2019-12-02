class Ip:
    """IP representation of the connection
    
    Attributes:
        addr_server: Server address and port.
    """
    def __init__(self):
        self._addr_server = (('localhost', 7000))

    @property
    def addr_server(self):
        """Returns server addres."""
        return self._addr_server
    