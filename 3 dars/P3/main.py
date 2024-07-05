"""
Barcha nol raqamlarni listning oxiriga o‘tkazing.
Sortlash amalidan foydalanmagan xolda.
Input:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]

Output:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0 , 0, 0]

"""

num = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

sum = [x for x in num if x != 0] + [x for x in num if x != 0]

print(sum)
