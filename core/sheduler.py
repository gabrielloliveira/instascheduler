from datetime import datetime
class Scheduler:
    def __init__(self):
        self._image = None 
        self._subtitle = None 
        self._location = None 
        self._account = None 
        self._created = None 
        self._date_scheduler = None

    """-----------------------------get-and-set-------------------"""
    @property
    def image(self):
        return self._image
   
    @image.setter
    def image(self,novo):
        self._image = novo
    
    @property
    def subtitle(self):
        return self._subtitle
   
    @subtitle.setter
    def subtitle(self,novo):
        self._subtitle = novo
    
    @property
    def location(self):
        return self._location
   
    @location.setter
    def location(self,novo):
        self._location = novo
    
    @property
    def account(self):
        return self._account
   
    @account.setter
    def account(self,novo):
        self._account = novo
    
    @property
    def created(self):
        return self._created
   
    @created.setter
    def created(self):
        self._created = datetime.today()
    
    
    @property
    def date_scheduler(self):
        return self._date_scheduler
   
    @date_scheduler.setter
    def date_scheduler(self, dateHour):
        self._date_scheduler = datetime.strptime(dateHour,"%d/%m/%Y %H:%M")
    
    """----------------------------other-method---------------------"""
    def get_status(self):
        pass

