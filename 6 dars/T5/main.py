""" 
Map va Lambda funksiyasi orqali listni ichidagi tuplening ma'lumotlarning 2 elementi bo'yicha o'sish tartibida saralang.
Input:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Output:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

T1 dan T5 gachan uyga vazifalar boshqa fileda qilib, main.py fileda import qilib ishlating.

"""
data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorted(data, key=lambda x: x[1]))


