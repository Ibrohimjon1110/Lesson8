""" 
100dan kichik sonlar ichidan raqamlari tarkibida 
3 raqami qatnashgan barcha sonlarni va shu sonlar
sonini chiqaring.
Javob : 0:100 -> {3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37,
38, 39, 43, 53, 63, 73, 83, 93}
Soni: 19ta

"""

num = '3'

temp = []

for number in range(100):
    if num in str(number):
        temp += [number]  

son = "0-100 oralig'ida " + num + " raqami qatnashgan sonlar: {"
for i in range(len(temp)):
    son += str(temp[i])
    if i != len(temp) - 1:
        son += ", "
son += "}"
print(son)

print(f"Soni: {len(temp)} ta")

