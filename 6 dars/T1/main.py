""" 
Foydalanuvchi ketma-ket istalgan miqdorda int tipidagi sonlarni c harfini kiritmaguncha kiritadi. 
c kiritganda yigindini chiqarsin.
Maqsadingiz shu sonlar yig'indisini topish.
Foydalanuvchi sondan yoki c harfidan boshqa qiymat kiritsa
ValueError except ishlatiladi. Ya'ni faqat c yoki butun son kiriishini ekranga chiqarsin.

"""

yigindi = 0 
while True:
    try:
        num = input("Son kiriting: ")
        if num == 'c':
            print(f"Yigindi:{yigindi}")
            break
        else:
            yigindi+=int(num)
    except ValueError:
        print("Faqat c yoki butun son kiritish mumkin")    
        