import numpy as np
from User import *

class Wallet:
    def __init__(self, walletID, Sodu):
        self.IDWallet = walletID
        self.Sodu = Sodu

    def getIDWallet(self):
        return self.IDWallet
    
    def getSodu(self):
        return self.Sodu
    
    def setSodu(self, newSodu):
        self.Sodu = newSodu
    
