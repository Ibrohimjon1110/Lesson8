""" 
100dan kichik sonlar ichidan 
raqamlari bir-biriga teskari bo’lgan tub sonlarni chiqaring. 
Masalan: 13<--->31
"""

def tup(n):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False  
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

for num in range(2, 100):
    son = int(str(num)[::-1])  
    if tup(num) and tup(son):
        print(f"{num} <--> {son}")
