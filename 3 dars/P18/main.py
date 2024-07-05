""" 
Har xil uzunlikdagi Listlar berilgan va sizning 
vazifangiz ushbu listlarni quyidagi shartlar asosida yangi 
listga birlashtirish. Yangi listga birinchi list1 elementi 
va keyin list2 elementini ketma-ketlikda joylashtiring.
Input: list1=[1, 2, 3]   list2=[11, 22, 33]
Output: list3=[1, 11, 2, 22, 3, 33]
       
Input: list1=[1, 2, 3, 4, 5]   list2=[11, 22, 33]
Output: list3=[1, 11, 2, 22, 3, 33, 4, 5]

Input: list1=[1, 2]   list2=[11, 22, 33, 44, 55]

"""
list1 = [1, 2, 3]
list2 = [11, 22, 33]
num = []

for i in range(max(len(list1), len(list2))):
    if i < len(list1):
        num.append(list1[i])
    if i < len(list2):
        num.append(list2[i])

print(num)  

list1 = [1, 2, 3, 4, 5] 
list2 = [11, 22, 33]
num = []

for i in range(max(len(list1), len(list2))):
    if i < len(list1):
        num.append(list1[i])
    if i < len(list2):
        num.append(list2[i])

print(num)  

list1 = [1, 2] 
list2 = [11, 22, 33, 44, 55]
num = []

for i in range(max(len(list1), len(list2))):
    if i < len(list1):
        num.append(list1[i])
    if i < len(list2):
        num.append(list2[i])

print(num)  