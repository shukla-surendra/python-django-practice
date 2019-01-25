class Sharing_Test:
    list_data = []
    growth_rate = 1.5

x = Sharing_Test()
y = Sharing_Test()
x.list_data.append(1)
x.list_data.append(2)
y.list_data.append(3)
y.list_data.append(4)

print(x.list_data, y.list_data)
x.growth_rate= 2
print(x.growth_rate, y.growth_rate)