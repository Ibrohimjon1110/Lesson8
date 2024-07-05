""" 
Foydalanuvchi ketma-ket istalgan miqdorda int tipidagi sonlarni 
c harfini kiritmaguncha kiritadi.
Maqsadingiz shu sonlar yig'indisini topish.
Input: 1
            2
            3
            c
Output: 6

"""
son = 0

while True:
    number = input("Son kiriting ('c' ni yozib tugating): ")
    if number.lower() == 'c':
        break
    if number.isdigit():
        son += int(number)

print("Yig'indisi:", son)

