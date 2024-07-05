
'''
Bo’luvchilar soni aniq 9ga teng bo’lgan 1000 dan kichik barcha sonlarni toping:
Masalan: 36 (1, 2, 3, 4, 6, 9, 12, 18, 36)

'''

def bolovchilar_soni(son):
    sanoq = 0
    for i in range(1, son + 1):
        if son % i == 0:
            sanoq += 1
    if sanoq == 9:
        print(son)
            
for i in range(1, 1000):
    bolovchilar_soni(i)

