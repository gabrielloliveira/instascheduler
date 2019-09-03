class Bd:
    def __init__(self):
        self._accounts = []
        self._instagram = []
        self._publication = []

    @property
    def accounts(self):
        return self._accounts
    
    @accounts.setter
    def accounts(self,new):
        self._accounts.append(new)
    
    @property
    def instagram(self):
        return self._instagram
    
    @instagram.setter
    def instagram(self,new):
        self._instagram.append(new)

    @property
    def publication(self):
        return self._publication
    
    @publication.setter
    def publication(self,new):
        self._publication.append(new)
