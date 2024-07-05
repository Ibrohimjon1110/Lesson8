""" 
1 +11 + 111 + 1111 + .. n hadlar qatorining 
yig'indisini topish dasturini yozing.
Test:
n= 5
Kutilayotgan natija:
1 + 11 + 111 + 1111 + 11111
Sum: 12345

"""
n = int(input("n ni kiriting: "))  

num = 0  
number = 0  

temp = ""  

for i in range(1, n + 1):
    number = number * 10 + 1  
    num += number  
    temp += str(number) 
    if i != n:
        temp += " + " 

print(temp)
print("Sum:", num)


