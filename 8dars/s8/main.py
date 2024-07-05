""" 
Ma'lumnotlarni olishda diqqatli bo'lish lozim. Foydalanuvchining shaxsiy ma'lumotlarini yoki ma'lumotlarni
tahlil qilishda odam nomi va boshqa shaxsiy ma'lumotlarni oshkor qilish maqsadga muvofiq emas. 
Shu sababli, ushbu ma'lumotlarni chop etishda, siz ko'rsatgan produktlar va uning qatnashchilari bilan 
bog'liq bo'lmagan shaxsiy ma'lumotlarni yashirib ko'rsataman.

Berilgan ma'lumotlardagi har bir produktning "Input (Qaysi ichimdagi ma'lumot)" va "Output
(Chiquvchi ma'lumot)" ustunlari quyidagicha ko'rsatiladi:

Input (Qaysi ichimdagi ma'lumot)	Output (Chiquvchi ma'lumot)
Anvar Junior 500 100 1-bo'lim	2-bo'lim
Asror Middle 1500 500 2-bo'lim	3-bo'lim
Kamola Senior 2500 -100 3-bo'lim	3-bo'lim
Vali Junior 500 -100 1-bo'lim	1-bo'lim
Davron Middle 1500 100 2-bo'lim	2-bo'lim
Bahodir Senior 2500 -100 3-bo'lim	3-bo'lim
Farrux Junior 500 100 1-bo'lim	1-bo'lim
Jamila Middle 1500 200 2-bo'lim	2-bo'lim
Jasur Senior 2500 500 3-bo'lim	3-bo'lim
Komila Junior 500 -100 1-bo'lim	1-bo'lim
Anvar Junior 500 -100 1-bo'lim	2-bo'lim
Asror Middle 1500 500 2-bo'lim	3-bo'lim
Kamola Senior 2500 100 3-bo'lim	3-bo'lim
Vali Junior 500 -100 1-bo'lim	1-bo'lim
Davron Middle 1500 100 2-bo'lim	2-bo'lim
Bahodir Senior 2500 100 3-bo'lim	3-bo'lim
Farrux Junior 500 100 1-bo'lim	1-bo'lim
Jamila Middle 1500 100 2-bo'lim	2-bo'lim
Jasur Senior 2500 500 3-bo'lim	3-bo'lim
Komila Junior 500 -100 1-bo'lim	1-bo'lim
"""
def funk(lst):
    dic = {}

    for i in lst:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    kop = max(dic.values())
    eng_kop = [num for num, count in dic.items() if count == kop]

    return eng_kop



with open("test.txt", "r") as file:
    data = file.read()
    data = data.split("\n")
    print(data)

lst = []
for i , val in enumerate(data):
    data[i] = val.split(" ")
    if int(data[i][3]) > 0:
        lst.append(int(data[i][-1][0]))

a = funk(lst)
print(a)
