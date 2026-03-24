class User:
    def __init__(self, userID, fullName, walletID):
        self.userID = userID #int
        self.fullName = fullName #String
        self.walletID = walletID #int

    def set_ID_user(self, setID):
        self.userID = setID
    
    def set_fullName(self, setName):
        self.fullName = setName
    
    def set_walletID(self, setWalled_ID):
        self.walletID = setWalled_ID
    
    