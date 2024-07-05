""" 
Belgilangan List raqamlarini undan juft raqamlarni olib tashlagandan 
so'ng chop etish uchun Python dasturini yozing. 

Namuna roʻyxati :  lst = [23, 44, 56, 99, 111, 23, 54]
Kutilayotgan natija: [23, 99, 111, 23]

"""
lst = [23, 44, 56, 99, 111, 23, 54]

sum = [num for num in lst if num % 2 != 0]

print("Kutilayotgan natija:", sum)
