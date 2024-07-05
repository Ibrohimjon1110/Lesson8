
'''
S4:
booking_data.txt faylida quyidagi ma'lumotlar keltirilgan
id - ID raqami
departure - uchib ketish davlati
d_time - uchish vaqti
arrive - qo'nish davlati
a_time - qo'nish vaqti
cost - bilet narxi

1. Foydalanuvchi o'zida bor taxminiy pul miqdorini kiritadi. 
Maqsadingiz shu kiritlgan summadan $50 arzonroq va $100 qimmatroq bo'lgan biletlar ro'yhatini ko'rsatish


2. Kiritilgan davlat bo'yicha barcha aviareyslarni toping. 
Lekin chiqishda faqat soat 12:00dan 21:00gacha bo'lgan reyslar chiqsin.

3. Tasavvur qiling foydalanuvchi boshqa shahardan uchib kelmoq Lekin u shunday bir qiziq shartni aytadi:
- Men US davlatiga uchishim kerak. Meni har kuni soat 21:00da Zoomda meetingim bo'ladi. 
Shunga menga shunday reys tanlab beringki, qo'nish vaqti meetingdan kamida 1 soat oldin bo'lsin.
Menga shu reyslarning barchasini ko'rsatsangiz, uchish vaqti qiziq emas.

Shu shartlarga javob beruvchi barcha reyslarni toping.

'''

try:
    samm = float(input("Pul miqdorini kiriting: "))
except ValueError:
    print("Noto'g'ri kiritinggiz. raqam kiriting.")
    exit()

try:
    with open("booking_data.txt", "r", encoding="utf-8") as file:
        data = [line.strip().split(",") for line in file.readlines()] 
        for temp in data:
            temp[5] = float(temp[5].replace("$", "")) 
except ValueError:
    print("Fayl natug'ri.")
    exit()

print("\nPuga qarab buyutmalariggiz:")
for temp in data:
    if (samm - 50) < temp[5] < (samm + 100):
        print(temp)
        
print("\nDavlat va vaqtni tug'ri keluvchi buyurtmalar:")
num = input("Kodni kiriting (masalan, AQSh): ").upper()
for temp in data:
    try:
        time = int(temp[2].split(":")[0])  
        if 12 <= time < 21 and temp[3] == num:
            print(temp)
    except IndexError:
        print(f"Xato kiritinggiz: {temp}")

print("\nAQSh va vaqti 20:00 bo'lgan buyurtmalar:")
for temp in data:
    try:
        time = int(temp[4].split(":")[0])  
        if temp[1] == "US" and time == 20:
            print(temp)
    except IndexError:
        print(f"Xato kiritinggiz: {temp}")
