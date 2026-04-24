import numpy as np
import Wallet as wl

class MyBackup():
    # Save information by month, each month has each wallet
    def __init__(self, FullName, ListThang = np.arange(1, 13)):
        self.myName = FullName
        self.myMonth = ListThang
        self.ListTien = np.array([]) # TongCT = Tong Chi tieu
    
    def DieuKienNhap(self, input) -> bool:
        try:
            input = int(input)
            if(input >= 0 and input <=11):
                return True
            return False
        
        except TypeError as e: # Phong truong hop dau vao la String
            print("Loi nhap so Month xin hay nhap lai")
        
        except ValueError as err:
            print("Loi nhap so Month xin hay nhap lai")

    def setTien(self, Money, Month):
        Month -= 1
        self.resetMoneyMonth(Month)
        if(self.DieuKienNhap(Month)):
            self.TongCT[Month] += Money
        else:
            return

    def getTien(self, Month):
        Month -= 1
        if(self.DieuKienNhap(Month)):
            return self.TongCT[Month]
        else:
            return 0
    
    def printInfo(self):
        for i in range(12):
            print(f"Thang {i + 1}: ", self.TongCT[i])

    def resetMoneyMonth(self, Month):
        # Lenh nay duoc viet ra nham truong hop bi loi chuong trinh
        # VD cac truong hop nhu Money dang 3000 nhung loi thuat toan thi se reset lai
        Month -= 1
        if(self.DieuKienNhap(Month)):
            self.TongCT[Month] = 0

