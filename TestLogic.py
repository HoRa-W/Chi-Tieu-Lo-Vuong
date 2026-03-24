import pandas as pd
import numpy as np
import unicodedata

BANG_XOA_DAU = str.maketrans(
    "ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴáàảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ",
    "A"*17 + "D" + "E"*11 + "I"*5 + "O"*17 + "U"*11 + "Y"*5 + "a"*17 + "d" + "e"*11 + "i"*5 + "o"*17 + "u"*11 + "y"*5
)

def xoa_dau(txt: str) -> str:
    if not unicodedata.is_normalized("NFC", txt):
        txt = unicodedata.normalize("NFC", txt)
    return txt.translate(BANG_XOA_DAU)

# Warning please read this before apply for your's sample
# Use to convert money have format is +/- <number>k/20000 <Things common>


def ConvertToMoney(input) -> int:
    # input at here, type is string
    # This function will be use in case the paragram has "k" in their words
    # It means before "k" must be <10000 (max lenght only 4)
    try:
        # Create a variable used to check input is number 10000 or 10k to distingush it
        check = input.split(" ")

        if(check[1].find("k")  != 0): #Check is there k or not k
            sum = input.split("k")
            check_punctuation = sum[0].split(" ")
            #---------------------------------------------
            # Comparasion with + to find out that is positive or negative
            if (check_punctuation[0] == "+"):
                punctuation = 1
            else:
                punctuation = -1
            #---------------------------------------------
            sub = sum[1].split(" ") #Find for number after k letter
            sum = sum[0].split(check_punctuation[0])
            if not (sub[0] >= "0" and sub[0] <="9"):
                sub[0] = 0
            
            return punctuation * (int(sum[1]) * 1000 + int(sub[0]) * 100)
        else:
            sum = input.split(" ")
            #sum[0] check +/-
            #sum[1] Number
            if (sum[0] == "+"): return int(sum[1]) 
            else:
                return -int(sum[1])
    
    except ValueError:
         print("Oops!  That was no valid value.  Try again...")

#   This function use to summarize the goods
def ManageThings(nameFile = "H:\lamqualo\ChiTieuLoVuong\Test.txt"):
    sum = 0 # Remember to put sum inside function because interpretor maybe forgot it (i don't know) 
    with open(nameFile, encoding="utf-8") as f:
        for content in f:
            content = xoa_dau(content)
            sum += ConvertToMoney(content)
        print(sum)

ManageThings()
