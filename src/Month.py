import numpy as np

class Month():
    def __init__(self,FullName, ListThang = np.arange(1, 13), ListTien = np.zeros(12)):
        self.myName = FullName
        self.myMonth = ListThang
        self.TongCT = ListTien # TongCT = Tong Chi tieu
    
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
        print("Thong bao chi tieu cua", self.myName)
        for i in range(12):
            print(f"Thang {i + 1}: ", self.TongCT[i])

ok = Month()
ok.setTien(123, 1)
ok.setTien(432, 5)
ok.setTien(2222, 9)
ok.setTien(23, 12)
ok.printInfo()
