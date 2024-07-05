""" 
Foydalanuvchidan N sonini qabul qiling, 
va son tashkil topgan raqamlar ichidan toqlarini ekranga chiqaring.
Input: 12458864
Output: 1  5

"""

number = input("Istalgan sonni kiriting: ")

num = []

for son in number:
    if son in '13579':
        num += son + ' '


if num:
    print("Output:", num[:-1]) 
else:
    print("Output:")

