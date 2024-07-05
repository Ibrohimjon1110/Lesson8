""" 
Foydalanuvchidan 6 ta so`z kiritadi, maqsadingiz klaviaturaning bir qatorida joylashgan harflardan tashkil topgan so`zlarni alohida listga solib chop etish.

Input:["Hello","Alaska","Dad","Peace"]
Output: ["Dad","Alaska"]

Izoh:Dad - so`zi klaviaturaning, faqat ikkinchi qatoridagi harflardan tashkil topgan.

"""
num = set('asdfghjkl')

x = []
for i in range(6):
    sum = input(f"So'zni kiriting {i+1}: ")
    x.append(sum)

numbers = []

for sum in x:
 
    num2 = sum.lower()
    
    if all(char in num for char in num2):
        numbers.append(sum)

print("so'zlar:", numbers)

