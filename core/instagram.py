class Instagram:

    accounts = list()
    def __new__(cls, username):
        if not username in Instagram.accounts:
            Instagram.__instance = object.__new__(cls)
            username = username.lower()
            Instagram.accounts.append(username)
            Instagram.__instance._username = username
        else:
            raise Exception('Já existe esse usuário')  

    def __init__(self):
        self._username = None
        self._password = None
        self._user = None

    """-----------------------------get-and-set-------------------"""
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, valor):
        self._username = valor
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, valor):
        self._password = valor
        
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, valor):
        self._user = valor

    """----------------------------other-method---------------------"""
    def get_last_posts(self):
        pass
