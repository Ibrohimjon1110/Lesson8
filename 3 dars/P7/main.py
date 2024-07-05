""" 
Gilven
list1 = [10,20,[300,400,[5000,6000],500],30,40]

Expexted output:
[10,20,[300,400,[5000,6000,7000],500],30,40]
Berilgan listga 6000 dan keyin 7000 ni qo'shib qo'ying (xuddi rasmdagidek)..
"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)
