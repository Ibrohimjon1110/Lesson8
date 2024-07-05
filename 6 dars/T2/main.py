""" 
Foydalanuvchi istlagan xonali son kiritadi va sizning vazifangiz ushbu sonni birliklar, 
o’nliklar, yuzliklar va hokazo xonalar yig’indisi yoyilmasiga aylantirib chiqaradigan funksiya tuzish.
strga yig'ib qaytarsin.
input: 123          
output: 100+20+3      
input: 4213
output: 4000+200+10+3

"""
def yigindi_strga(son):
    son_str = str(son)
    yigindi = ""
    for i in range(len(son_str)):
        xonali_yigindi = int(son_str[i]) * 10**(len(son_str)-i-1)
        if i == len(son_str)-1:
            yigindi += str(xonali_yigindi)
        else:
            yigindi += str(xonali_yigindi) + "+"
    return yigindi

son = int(input("Son kiriting: "))
yigindi = yigindi_strga(son)
print(yigindi)
