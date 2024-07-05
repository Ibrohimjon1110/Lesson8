"""

Toq indexdagi qiymatlarni kvadratga ko'tarib o'ziga o'zlashtiring
Input:  
[
       [2,  15,  4],
       [19, 24, 11],
       [7,   9,  5],
       [10,  3,  1]
]

Output: 
[
       [2,  225,  4],
       [19, 576, 11],
       [7,   81,  5],
       [10,   9,  1]
]

    """
matrix = [
    [2, 15, 4],
    [19, 24, 11],
    [7, 9, 5],
    [10, 3, 1]
]

num = []

for i in range(len(matrix)):
    sum = matrix[i]
    number = []
    for j in range(len(sum)):
        if j % 2 != 0:  
            number.append(sum[j] ** 2)
        else:
            number.append(sum[j])
    num.append(number)

for sum in num:
    print(sum)
