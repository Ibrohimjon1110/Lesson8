""" 
Sample list :[11,33,50]
Exprected Output :11350
Ixtiyoriy listdagi sonlarni bitta songa aylantirib qo'ying.
Son INT da bo'lsin.

"""

x = [11, 33, 50]

num = int("".join(map(str, x)))
print(num)
