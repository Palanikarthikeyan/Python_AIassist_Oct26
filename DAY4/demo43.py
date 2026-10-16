class Pa:
    def __init__(self):
        print("Welcome to class Pa")
        
class Pb(Pa):
    def method(self):
        return None
    
obj = Pb() # ->Welcome to class Pa

## Vs
class Pa:
    def method(self):
        return None

class Pb(Pa):
    def __init__(self):
        print("Welcome to class Pb")
        
obj = Pb() # -> Welcome to class Pb
obj.method() # calling parent class method ->None
