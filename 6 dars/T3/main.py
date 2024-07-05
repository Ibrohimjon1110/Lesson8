""" 
Kalkulyator dasturini tuzing. Asosiy bajarilishi shart bo'lgan amallar: +, -, *, /.
Dasturda ValueError va ZeroDivisionError tekshiruvi bo’lishi shart.
Input:
Num1: 7
Num2: 5
Operator: +
Output: 12

"""
num1 = float(input("1 chi sonini kiriting: "))
amallar = input("amalni kiriting: ")
num2 = float(input("2 sonini kiriting: "))


result = None

try:
    if amallar == '+': print(num1 + num2)
    elif amallar == '-':print(num1 - num2)
    elif amallar == '*':print(num1 * num2)
    elif amallar == '/':print(num1 / num2)
except ValueError:
    print("Xato kiritish")
    
except ZeroDivisionError:
    print("Nolga bo'linmaydi")
