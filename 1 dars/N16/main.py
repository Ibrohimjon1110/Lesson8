""" 
Foydalanuvchi faqat kichik harf kiritadi, vazifangiz ushbu harf ingliz alfabetida nechanchi orinda turganini aniqlash.
Input: c
Output: Alfabetda 3-orinda turadi.

"""

harf = input("Kichik harf kiriting: ")


harf_tartibi = ord(harf) - ord('a') + 1

print(f"Alfabetda {harf_tartibi}-orinda turadi.")
