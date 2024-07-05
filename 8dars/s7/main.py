""" 
Foydalanuvchi tomonidan Dictionaryga keyga ismlar va valuega esa Boolean type (1 yoki 0) kiritadi. 
Sizning vazifangiz eng ko’p ovoz berganlarning ismlarini chiqarish.
Agar durang bo’lsa, ikkalasini ham chiqarish kerak.
Chiqarsishda birinchi qatorda qaysi qiymat ko’p ovoz berilganini va keying qatorda esa ismlarni chiqarish kerak.
Ma’lumotlarni chiqarish na’munada keltirilgandek bo’lishi kerak.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo’yiladi.

Input (Kiruvchi ma'lumot)	Output (Chiquvchi ma'lumot)
{'Anvar': 1, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	1 \n Anvar Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 1, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	0 \n Anvar Asror Surayyo
{'Anvar': 1, 'Lobar': 0, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	1 \n Lobar Vali Baxtiyor
{'Anvar': 0, 'Lobar': 0, 'Asror': 0, 'Vali': 1, 'Surayyo': 0, 'Baxtiyor': 1}	0 \n Anvar Lobar Asror Surayyo  
foydalanuvchidan olinsin
"""
def ovoz(dict):
    num = max(dict.values())
    print(num)
    names = [k for k, v in dict.items() if v == num]
    print(" ".join(names))

nam = {}
n = int(input("Berilgan soni kiriting: "))
for i in range(n):
    key = input("Ismni kiriting: ")
    value = int(input("Qiymatni kiriting (0 yoki 1): "))
    nam[key] = value

ovoz(nam)
