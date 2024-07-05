"""
Foydalanuvchi tomonidan Listda faqat butun sonlardan iborat List kiritilgan. 
Sizning vazifangiz ushbu Listda qo'shni bir xil ishorali elementlarni chiqaring.
Agar qo'shni elementlarning ishoralari bir biridan farqli bo'lsa, sonlar chiqarilmasin.
Har bir masala shartiga mos qo'shni elementlarni alohida qatorda chiqarlisin.

Eslatma: Barcha ma'lumotlarni foydalanuvchi kiritishi lozim va algoritmsiz ishlangan misolga past ball qo'yiladi.

Input (Kiruvchi ma'lumot)	Output (Chiquvchi ma'lumot)
[-1, 2, 3, -1, -2]	2 3 \n -1 -2
[-1, 2, 3, -1, 4, 5, 6, 7]	2 3 \n 4 5 \n 5 6 \n 6 7

"""
def faqat_butun_sonlar(l):
    nonumber = set()
    for x in l:
        if isinstance(x, int):  
            nonumber.add(x)
    return sorted(nonumber)  

num = input("Butun sondan iborat  List kiriting: ")

try:
    sum = eval(num)
    if isinstance(sum, list):
        result = faqat_butun_sonlar(sum)
        print(", ".join(map(str, result)))
    else:
        print("Noto'g'ri kiritdingiz.")
except Exception as e:
    print("Xatolik yuz berdi:", e)