""" 
Satr uzunligi 2 va undan ortiq, birinchi va oxirgi belgilari bir xil 
bo‘lgan satrlar sonini hisoblavchi Python dasturini yozing. 
  Namuna roʻyxati : ['abc', 'xyz', 'bo'lib','aba', '1221']  
  Kutilayotgan natija: 3

"""
num = ['abc', 'xyz', 'bo\'lib', 'aba', '1221']

count = 0
for s in num:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Kutilayotgan natija:", count)
