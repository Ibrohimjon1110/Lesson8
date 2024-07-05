""" 
Foydalanuvchi string kiritadi. Shu stringdagi har bitta belgidan 
nechtadan borligini dictionary ga quyidagicha joylang:

Input:     "w3resource"
Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

"""
num = input("Satirni kiriting: ")

x = {}

for char in num:
    if char in x:
        x[char] += 1
    else:
        x[char] = 1

print(x)
