class User:
    ID = 0

    accounts = list()
    def __new__(cls, email):
        if not email in User.accounts:
            User.__instance = object.__new__(cls)
            email = email.lower()
            User.accounts.append(email)
            User.__instance._email = email
        else:
            raise Exception('Já existe esse usuário na plataforma')  

    def __init__(self):
        self._email = None
        self._password = None
        User.ID += 1
  
    @property
    def email(self):
        return self._email
  
    @email.setter
    def email(self, value):
        self._email = value
  
    @property
    def password(self):
        return self._password
  
    @password.setter
    def password(self, value):
        self._password = value