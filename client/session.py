from datetime import datetime
import json

class Session():
    __instance = None
    def __new__(cls, email):
        if Session.__instance is None:
            Session.__instance = object.__new__(cls)
            Session.__instance._user = email

        return Session.__instance
            
    @property
    def user(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                return data['user']

        except:
            return None        

    def set_data(self, email):
        data = {
            'user': email,
            'login_at': str(datetime.now())
        }
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
