def F2C(Fahrenheit):
    return (Fahrenheit-32)*5/9
    
for Fahrenheit in range(0,101,5):
    print(Fahrenheit, str(int(F2C(Fahrenheit))))
    
