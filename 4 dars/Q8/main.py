""" 
Foydalanuvchi rim raqamlarini kiritadi, vazifangiz, shu rim raqamlarini arab raqamlariga o`girish.
Input: "X"
Output: 10
Input: s = "LVIII"
Output: 58
Input: s = "MCMXCIV"
Output: 1994
Izoh: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

num = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
    'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
    'XC': 90, 'CD': 400, 'CM': 900
}

s = input(">>>>>: ")

i = 0
result = 0
n = len(s)

while i < n:
    if i + 1 < n and s[i:i+2] in num:
        result += num[s[i:i+2]]
        i += 2
    else:
        result += num[s[i]]
        i += 1

print(f"Alishtirilgani: {result}")

