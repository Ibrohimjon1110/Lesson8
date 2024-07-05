""" 
Foydalanuvchi listga istalgancha qiymat kiritadi, siz shu qiymatlar ichidan
faqat bir marta takrorlangan raqamlar sonini qaytaruvchi funksiya tuzing, unday sonlar yoq bolsa -1 qaytarsin.
Input:[4,1,2,1,2]
Output: 1
Input:[1,2,3,1,1]
Output: 2

"""
def name(nums):
    temp = set()
    for num in nums:
        if num in temp:
            return num
        temp.add(num)
    return -1

kiritish1 = [4, 1, 2, 1, 2]
chiqarish1 = name(kiritish1)
print(f"kiritilgan qiymat: {kiritish1}\nNatija: {chiqarish1}")

kiritish2 = [1, 2, 3, 1, 1]
chiqarish2 = name(kiritish2)
print(f"kiritilgan qiymat: {kiritish2}\nNatija: {chiqarish2}")
