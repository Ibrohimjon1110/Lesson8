""" 
Foydalanuvchi son kiritadi vazifangiz quyidagi shaklda faylga ma'lumot yozish, agar son toq bo`lsa:
Input: 5
Output:
1=1
2+2=4
3+3+3=9
4+4+4+4=16
5+5+5+5+5=25
Agar son juft bo`lsa:
Input: 4
4+4+4+4=16
3+3+3=9
2+2=4
1=1
"""
try:
    num = int(input("Son kiriting: ")) 
    if num <= 0:
        raise ValueError("Musbat son kiriting!")
    
    with open("sonlar.txt", "w") as file:
        if num % 2 != 0: 
            for i in range(1, num + 1):
                line = '+'.join([str(i)] * i) + '=' + str(i * i)  
                file.write(line + '\n')  
                print(line)  
        else:  
            for i in range(num, 0, -1):
                line = '+'.join([str(i)] * i) + '=' + str(i * i)  
                file.write(line + '\n')  
                print(line)  

except ValueError as ve:
    print(f"Xatolik: {ve}")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

