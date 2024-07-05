""" 
Foydalanuvchi sekundlarni kiritadi. Siz uning nechchi soat, minut va sekundligini ekranga chiqaring
Input:     4000
Output: 1 soat 6 min 40 sek
Input:    3600
Output: 1 soat 0 min 0 sek

"""

sekundlar = int(input("Sekundlarni kiriting: "))

soat = sekundlar // 3600
qoldiq_sekundlar = sekundlar % 3600
minut = qoldiq_sekundlar // 60
sekund = qoldiq_sekundlar % 60

print(f"{soat} soat {minut} min {sekund} sek")
