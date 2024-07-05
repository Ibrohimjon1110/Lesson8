""" 
Agar ikki natural sonlarning har biri ikkinchisining 
barcha boʻluvchilari yigʻindisiga teng boʻlsa doʻstona sonlar deyiladi.
50 000 dan kichik bo'lgan barcha do'stona sonlarni toping. 
Masalan, 220 (1+2+4+5+10+11+20+22+44+55+110=284) va 284 (1+2+4+71+142=220)
"""


number = []

for num in range(2, 50001):
    son = 0
 
    for i in range(1, num):
        if num % i == 0:
            son += i
    
    if son > num:
        sum = 0

        for i in range(1, son):
            if son % i == 0:
                sum += i

        if sum == num:
            number.append((num, son))

print("Do'stona sonlar:")
for temp in number:
    print(f"{temp[0]} va {temp[1]}", end=", ")

print("\nUmumiy soni:", len(number), "ta")

