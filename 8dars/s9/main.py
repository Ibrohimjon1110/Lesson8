""" 
My_sort nomli funksiyа yaratinq va ushbu funksiyaga parametr sifatida faqat butun sonlardan iborat List ma’lumotlari beriladi. 
Sizning vazifangiz bu funksiyaga qiymat qaytarish sifatida Listning har bir elementlarining raqamlar
yig’indisi bo’yicha o’sish tartibida saralash kerak. Foydalanuvchi List elementlariga faqat musbat 
sonlar kirita oladi va shuni shartini ham exception orqali tekshirib oling.

Eslatma: Barcha ma’lumotlarni foydalanuvchi kiritishi lozim va algoritmisiz ishlangan misolga past ball qo’yiladi.

Input (Kiruvchi ma’lumot)
My_sort([14, 30, 103])

Output (Chiquvchi ma’lumot)
[30, 103, 14]

My_sort([5, 31, 123, 80, 11])

Output (Chiquvchi ma’lumot)
[11, 31, 5, 123, 80]

"""
def noname(number):
    return sum(int(digit) for digit in str(number))

def My_sort(lst):
    for num in lst:
        if num <= 0:
            raise ValueError(" musbat butun sonlar kiriting.")

    return sorted(lst, key=noname)

try:
   
    name = eval(input("Musbat butun sonlardan iborat ro'yxatni kiriting: "))
    
    name = My_sort(name)
    print("Saralgan ro'yxat:",name)

except ValueError as e:
    print(e) 
except Exception as e:
    print("Xatolik yuz berdi:", e)

