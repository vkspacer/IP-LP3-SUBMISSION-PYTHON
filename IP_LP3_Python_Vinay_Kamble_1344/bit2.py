def leap(y):
    if(y%4==0):
        if(y%400==0):
            return True
        elif(y%100==0):
            return False
        else:
            return True
    else:
        return False
        
y=int(input())
print(leap(y))