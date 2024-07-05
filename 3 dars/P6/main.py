""" 
ikkala list da ham bor qiymatlarni ekranga chiqaring
numbers1 = [2,-1,5,-3,8,-4,6,7,9]
numbers2 = [1,6,7,-3,-9,-4,-5]
"""
numbers1 = [2,-1,5,-3,8,-4,6,7,9]
numbers2 = [1,6,7,-3,-9,-4,-5]

temp = []

for num in numbers1:
    if num in numbers2:
        temp.append(num)

print(temp) 