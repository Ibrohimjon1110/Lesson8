""" 
Foydalanuvchi biror soz kiritadi, vazifangiz shu soz uzunligiga teng bo`lgan sonning kubini topish.
Input:salom dunyo
Output: 1331

"""

soz = input("So'z kiriting: ")


uzunlik = len(soz)
kub = uzunlik ** 3
print(f"{soz} so'zi uzunligi {uzunlik} ga teng bo'lgan va uning kubi {kub} ga teng.")
