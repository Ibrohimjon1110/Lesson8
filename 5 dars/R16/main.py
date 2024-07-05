"""
isAnagram() function tuzing, bu function o`ziga ikki so`z qabul qilib, bu so`zlar anagram yoki yo`qligini aniqlasin.
NOTE: Anagram so`zlar, o`zaro bir xil harflardan tashkil topgan, ammo umuman boshqa boshqa so`zlar.

Input: anagram,nagaram
Output: True

Input: car,tac
Output: False

"""
def isAnagram(sum1, sum2):

    num1 = sorted(sum1)
    num2 = sorted(sum2)

    return num1 == num2

sum1 = "anagram"
sum2 = "nagaram"
print(isAnagram(sum1, sum2))  

sum1 = "car"
sum2 = "tac"
print(isAnagram(sum1, sum2))
