""" 
Sizga faqat raqamlardan iborat list beriladi siz uni raqamga o'girib birni qoshib list qilib qaytarishingiz kerak,

num:     [1,2,3]
Output: [1,2,4]
Tushuntirish: 123 ga birni qoshilsa 124 va siz [1,2,4] qilib qaytarishingiz kerak

Input      [9]
Output: [1,0]

Input:     [9,9,9,9]
Output: [1,0,0,0,0]

"""

num1 = [1, 2, 3]
num2 = [9]
num3 = [9, 9, 9, 9]

sum1 = []
sum2 = []
sum3 = []

def chiqar(nums):
    temp = 1
    x = []
    
    for num in reversed(nums):
        x = num + temp
        if x >= 10:
            x.insert(0, 0)
            temp = 1
        else:
            x.insert(0, x)
            temp = 0
    
    if temp > 0:
        x.insert(0, temp)
    
    return x

sum1 = chiqar(num1)
sum2 = chiqar(num2)
sum3 = chiqar(num3)

print("num:", num1)
print("sum:", sum1)

print("num:", num2)
print("sum:", sum2)

print("num:", num3)
print("sum:", sum3)
