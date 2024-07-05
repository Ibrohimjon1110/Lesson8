"""Foydalanuvchi son kiritadi, sonning raqamlar yig`indisi bir xonali bo`lib qolgancha hosil bo`lgan sonning raqamlar yig`indisini hisoblab yakuniy narijani chiqaring.

Input: 38
Output: 2
Tushuntirish: 38 => 3+8 => 11 => 1+1 = 2

Input:96
Output: 
Tushuntirish: 96 => 9+6 => 15 => 1+ 5 => 6"""

num = int(input("Sonni kiriting: "))

while num >= 10:
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    num = digit_sum

print(num)