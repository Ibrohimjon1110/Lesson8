""" 
users = [
 {
      Name: Asil,
      age: 9,
      cars: 3     
 },
{
      Name: Laziz,
      age: 19,
      cars: 2    
 },
{
     Name: Sardor,
     age: 25,
     cars:7
},
{
     Name: Og`abek,
     age: 5,
     cars:5
}
]

Quyidagi list ichidan Yoshi 18 dan katta va mashinasi 1 tadan ko`p hamma insonlar ismini chiqaruvchi function tuzing.

Keylarni barchasi str.

"""
def chiqar(users):
    num = []
    for user in users:
        if user['Name'] and user['age'] > 18 and user['cars'] > 1:
            num.append(user['Name'])
    return num


users = [
    {'Name': 'Asil', 
     'age': 9, 
     'cars': 3
    },
    {'Name': 'Laziz',
     'age': 19, 
     'cars': 2
    },
    {'Name': 'Sardor',
     'age': 25,
     'cars': 7
    },
    {'Name': 'Og`abek', 
     'age': 5, 
     'cars': 5
}
]

filtered_names = chiqar(users)
print(filtered_names)
