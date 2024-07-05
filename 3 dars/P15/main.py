""" 
1 dan n gacha bo'lgan oraliqda berilgan ro'yxatni birlashtirish orqali 
ro'yxat yaratish uchun Python dasturini yozing. Tahrirlovchiga   o'ting.
Namuna ro'yxati : ['p', 'q']
n =5
Namuna Chiqish : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4' , 'q4', 'p5', 'q5']

"""
lst = ['p', 'q']
n = 5

num = []
for i in range(1, n + 1):
    for x in lst:
        num.append(f"{x}{i}")

print("Natija ==>", num)
