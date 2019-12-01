from datetime import datetime
import json
import os

class Session():
    """Class to simulate logged in user session."""
    __instance = None
    def __new__(cls, email):
        """Singleton design standard to ensure only one client session will 
        be created

        Args:
            email: user's email.

        """
        if Session.__instance is None:
            Session.__instance = object.__new__(cls)
            Session.__instance._user = email

        return Session.__instance
            
    @property
    def user(self):
        """Method to return logged in user email.
        
        Returns:
            The function returns the user's email or if not found returns the
            value None
        """
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(BASE_DIR, "data.json")
        try:
            with open(json_path, 'r') as f:
                data = json.load(f)
                return data['user']

        except:
            return None        

    def set_data(self, email):
        """Method for saving logged user email in session file.
        
        Args:
            email: user's email.
        """
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(BASE_DIR, "data.json")
        data = {
            'user': email,
            'login_at': str(datetime.now())
        }
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
