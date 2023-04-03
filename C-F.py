def C2F(Celcius):
    return (Celcius*9/5)+32
    
for Celcius in range(0,101,5):
    print(Celcius, str(int(C2F(Celcius))))
    
