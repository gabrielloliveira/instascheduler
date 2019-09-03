from user import User
class CreateUser:
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
	def registering(self):
		user = User()
		user.email = self.email
		user.password = self.password
		return user

# ob = CreateUser()
# ob.email = "disgracaaaa"
# ob.password = "disgracaaaa2"
# obUser = ob.registering()
# print(obUser.email)
# print(obUser.password)
