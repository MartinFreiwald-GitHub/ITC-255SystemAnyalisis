from user import User

class Staff(User):
    def _init_(self, name, email, securityLevel, position):
        self.name=name
        self.email=email
        self.securityLevel=securityLevel
        self.position=position

    def getPosition(self):
        return self.position

     def _str_(self):
        return super(Staff, self)._str_() + ", " + self.position
