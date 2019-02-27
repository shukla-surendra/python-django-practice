amount = 1000
rate = 8.5
for i in range(1, 14):
    a = amount*(1+(rate/4))**4
    print(a)
    amount = a+1000