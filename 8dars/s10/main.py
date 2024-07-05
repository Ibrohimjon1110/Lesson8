"""
Tasavvur qiling-a, sizda berilgan naqshga muvofiq turli xil ranglar bilan to'ldirish kerak bo'lgan kvadratchalar qatori bor. Kvadratchalarni ketma-ket bo'yash kerak, ya'ni keyingi kvadrat boshqa rangda bo'lsa, qalamni o'zgartirishingiz kerak bo'ladi.

Eslatma: Barcha ma'lumotlarni foydanavchi kiritishi lozim va algoritmsiniz ishlangan misolga past ball qo'yiladi.

Ranglar ro'yxatini oladigan va butun naqshni to'ldirish uchun zarur bo'lgan vaqtning qiymatini (soniyalarda) qaytaradigan funksiyani yozing.

Bunda:

qalamni almashtirish uchun 1 soniya kerak bo'ladi
kvadratni to'ldirish uchun 2 soniya kerak bo'ladi
Input (Kiruvchi ma'lumot)
naqsh(["Red", "Blue", "Red", "Blue", "Red"])
naqsh(["Blue"])
naqsh(["Red", "Yellow", "Green", "Blue"])
naqsh(["Blue", "Blue", "Blue", "Red", "Red", "Red"])

Output (Chiquvchi ma'lumot)
14
2
11
"""
def hisobla_ranglar_vaqti(ranglar: str) -> int:
    lst = ranglar.split(" ")
    print(lst)
    
    noname = 2
  
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            noname += 3
        else:
            noname += 2
    
    return noname

ranglar = input("Ranglarni bo'sh joy tashlab kiriting: ")
umumiy_vaqt = hisobla_ranglar_vaqti(ranglar)
print("Umumiy vaqt:", umumiy_vaqt)

