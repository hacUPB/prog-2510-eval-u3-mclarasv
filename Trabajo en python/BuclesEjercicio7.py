print("-"*43)
print("Grados celsius\t|\tGrados fahrenheit")
print("-"*43)
for celsius in range(0,110,10):
    fahrenheit = (celsius*(9/5))+32
    print(f"{celsius}\t|\t{fahrenheit}")