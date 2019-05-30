class User();
    def _init_(self,name, email, securityLevel);
        self.name=name
        self.email=email
        self.securityLevel=securityLevel

    def getName(self);
        return self.name
    
    def getEmail(self);
        return self.email

    def getSecurityLevel(self);
        return self.securityLevel

    def _str_(self);
        return self.name + ", " + self.email
        