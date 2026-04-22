import numpy as np
from User import *

class Wallet:
    def __init__(self,userID, fullName, walletID, ListChiPhi, Sodu = 0):
        self.userID = User(userID, fullName, walletID)
        self.IDWallet = walletID
        self.ListChiPhi = ListChiPhi
        self.Sodu = Sodu
    
