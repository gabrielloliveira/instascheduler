class User:
	def __init__(self):
		self._email = None
		self._password = None
	
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
		self.password = valor