import numpy as np
from Month import *
import Wallet as wl

class User:
    def __init__(self, userID, fullName, walletID):
        self.userID = userID #int
        self.fullName = fullName #String
        self.myWallet = wl.Wallet(walletID, np.array([]), 0)
        self.TimeLine = Month(fullName)
    
    def printUser(self):
        print("Hello", self.fullName)
        print("Here is your TimeLine")
        self.TimeLine.printInfo()



    
    