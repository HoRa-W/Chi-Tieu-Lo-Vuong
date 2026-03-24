import pandas as pd
import numpy as np

def ConvertToMoney(input) -> int:
    # input at here, type is string
    # This function will be use in case the paragram has "k" in their words
    # It means before "k" must be <10000 (max lenght only 4)
    try:
        #Make a clear translate
        input.translate
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
            #sum[0] xet dau
            #sum[1] xet so
            if (sum[0] == "+"): return int(sum[1])
            else:
                return -int(sum[1])
    
    except ValueError:
         print("Oops!  That was no valid value.  Try again...")
    
sum  = 0
with open("H:\lamqualo\ChiTieuLoVuong\Test.txt") as f:
    for x in f:
        sum += ConvertToMoney(x)

print(sum)
