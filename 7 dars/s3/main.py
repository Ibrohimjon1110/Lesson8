""" 
product_material.txt bazasida sizda
id - produkt ID raqami
product - produkt kodi
material - ishlab chiqarilgan materiali
price - narxi
is_available - omborda bor yo'qligi
berilgan

1. Maqasadingiz shu ma'lumotlar orasidan narxi 500 va 1000 dollar orasida bo'lgan va omborda mavjud bo'lgan produktlar ID raqami va ishlab chiqarilgan materialini chop etish bo'ladi.

2. Foydalanuvchi material nomini kiritadi va siz unga barcha omborda hozirda mavjud (true) bo'lgan produktlar narxlarini o'sish tartibida chiqarib berishingiz lozim

3. Omborda mavjud bo'lmagan (ya'ni false bo'lgan)  va narxi 1000 dollardan arzon bo'lgan tovarlarning ishlab chiqarilgan materialini ekranga chop eting.
"""
with open('product_material.txt', 'r') as file:
    data = []
    for line in file:
        if line.strip():
            nonem = line.strip().split(',')
            nonem[3] = float(nonem[3].replace('$', ''))
            nonem[4] = nonem[4].strip().lower() == 'true'
            data.append(nonem)

print("Narxi 500 dan 1000 dollargacha bo'lgan mahsulotlar va mavjud:")
for item in data:
    if 500 < item[3] < 1000 and item[4]:
        print(f"ID: {item[0]}, Material: {item[2]}")

material = input(" material nomini kiriting: ")
num = [item for item in data if item[2] == material and item[4]]
temp = sorted(num, key=lambda x: x[3])

print(f"Materiallar bilan barcha mavjud mahsulotlar'{material}' narx bo'yicha saralangan:")
for i in temp:
    print(f"i ID: {i[0]}, Narxi: ${i[3]}")

print("Mavjud bo'lmagan mahsulotlar materiallari va narxi < $1000:")
for item in data:
    if not item[4] and item[3] < 1000:
        print(f"Material: {item[2]}")
