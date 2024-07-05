""" 
Berilgan listni shunday yangilangki, qiymatlar takrorlanmasin

Input:        [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
Output:     [2, 5, 1, 4, 3, 6, 8, 7, 9]

"""
num = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]

sum = []
for x in num:
    if x not in sum:
        sum.append(x)

print(sum)

