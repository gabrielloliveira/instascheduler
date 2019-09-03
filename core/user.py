class User:
    ID = 0
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