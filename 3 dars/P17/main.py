""" 
Berilgan ro'yxatda elementlarni o'sish , kamayish yoki tartibsiz joylashganini aniqlovchi dastur tuzing.

Input: [5,3,8,1]
Output: tartibsiz

Input: [1,4,7,9]
Output: o'sish

"""

arr1 = [5, 3, 8, 1]


num = True
sum = True

for i in range(len(arr1) - 1):
    if arr1[i] > arr1[i + 1]:
        num = False
    if arr1[i] < arr1[i + 1]:
        sum = False

if num and not sum:
    print("o'sish")
elif sum and not num:
    print("kamayish")
else:
    print("arr1 tartibsiz:")
#================================================================
arr2 = [1, 4, 7, 9]
num = True
sum = True

for i in range(len(arr2) - 1):
    if arr2[i] > arr2[i + 1]:
        num = False
    if arr2[i] < arr2[i + 1]:
        sum = False

if num and not sum:
    print("arr2 o'sish:")
elif sum and not num:
    print("kamayish")
else:
    print("tartibsiz")
