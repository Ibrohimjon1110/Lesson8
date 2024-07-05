"""Foydalanuvchidan mamlakat yer maydoni va aholi sonini qabul qiling.
Va mamlakat yer maydoni zichligini chop eting.

    """
    
mamlakat_ismi = input("Mamlakat nomini kiriting: ")
maydon_km2 = float(input(f"{mamlakat_ismi}ning yer maydonini km²da kiriting: "))
aholi_soni = int(input(f"{mamlakat_ismi}ning aholi sonini kiriting: "))

zichlik = aholi_soni / maydon_km2

print(f"{mamlakat_ismi}ning yer maydoni: {maydon_km2} km²")
print(f"{mamlakat_ismi}ning aholi soni: {aholi_soni}")
print(f"{mamlakat_ismi}ning zichligi: {zichlik} kishi/km²")

