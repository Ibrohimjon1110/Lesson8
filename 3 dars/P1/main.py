""" 
Berilgan list ni shunday yangilangi, list elementlarining o'rninga shu list elementlarining tiplari joylashib qolsin
Agar, berilga list:
[True, "Salom", 5, 5.6]
bo'lsa

Natija: 
[<class 'bool'>, <class 'str'>, <class 'int'>, <class 'float'>]

Task Point BF 79, [24.06.2024 12:30]

"""
x = [True, "Salom", 5, 5.6]
sum = [type(num) for num in x]
print(sum)
