""" 
Rasmdagi kabi ichma ich list berilgan. Siz esa, qaysi qatordagi elementlar 
yig'indisi eng katta bo'lsa o'sha yig'indini chiqaring.
numbers = [
    [5,3,7]
    [1,4,9]
    [2,8,6]
]
Output: 16     (chunki 2+8+6=16)
"""
numbers = [
    [5, 3, 7],
    [1, 4, 9],
    [2, 8, 6]
]

num = float('-inf')  

for temp in numbers:
    x = sum(temp)  
    if x > num:
        num = x

print(num)
