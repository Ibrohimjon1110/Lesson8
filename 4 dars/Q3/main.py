""" 
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
expexcted output
{70,40,50,20,60,30}
Ikkala set ni qo'shgandan keyin unique 
qiymatlarni ekranga chiqaring (xuddi rasmdagidek)

"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
num = set1.union(set2)
print(num)
