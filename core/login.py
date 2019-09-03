class Login:
    def __init__(self):
        self._email = None
        self._password = None

    """-----------------------------get-and-set-------------------"""
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        self._email = valor
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, valor):
        self._password = valor

    """----------------------------other-method---------------------"""
    def data_verification(self, bd):
        return self.query_accounts(bd)
        
    def query_accounts(self, bd):
        for i in bd.accounts:
        if i.email == self.email:
            if i.password == self.password:
                return i
        return False
            
