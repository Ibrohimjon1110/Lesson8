"""
Bizga list berilgan va foydalanuchi tomonidan bitta son kiritiladi. 
Agarda ikkita elementining yig'indisi kiritilgan songa teng bo'lsa 
shu elementlarning indexlarini ekranga chiqaruvchi dastur tuzing.
lst = [1, 2, 33, 5, 6, 7, 7]
INPUT = 3
lst[0]+lst[1] = 3
OUTPUT = 0 , 1

INPUT = 8
lst[0]+lst[5] = 8
lst[0]+lst[6] = 8
lst[1]+lst[4] = 8
OUTPUT = 
0 , 5
0 , 6
1 , 4

    """



lst = [1, 2, 33, 5, 6, 7, 7]
num = int(input("Kiritilgan son: "))

result = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == num:
            result.append((i, j))

if result:
    print(", \n".join(f"{i} , {j}" for i, j in result))
else:
    print(" qo'shiluvchilar yo'q")