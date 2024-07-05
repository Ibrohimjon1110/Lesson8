"""
Miyyani ishlatamiz.If kerakmas!
Foydalanuvchi butun son kiritadi. Bu son musbat bo'lsa manfiyga, manfiy bo'lsa musbat qilib ekranga chiqaring.
Input: -85
Output: 85
—————————————————————
Input: 48
Output: -48

    """
def manfiyga_ozgartir(son):
    
    return -son if son >= 0 else abs(son)

son = int(input("Butun sonni kiriting: "))

natija = manfiyga_ozgartir(son)
print(f"Natija: {natija}")
