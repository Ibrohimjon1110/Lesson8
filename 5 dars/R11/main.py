""" 
Uchta list ni quyidagicha birlashtiruvchi function tuzing:
Input:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Output:
[
     {'S001': {'Adina Park': 85}},
     {'S002': {'Leyton Marsh': 98}},
     {'S003': {'Duncan Boyle': 89}},
     {'S004': {'Saim Richards': 92}}
]
Note: natijada list ichida dictionary lar xosil bo'lgan

"""

def natija(temp):
    for num in temp:
        sum = list(num.keys())[0]
        x = num[sum]
        dp = list(x.keys())[0]
        name = x[dp]
        print(f"{{'{sum}': {{'{dp}': {name}}}}},")

temp = [
    {'S001': {'Adina Park': 85}},
    {'S002': {'Leyton Marsh': 98}},
    {'S003': {'Duncan Boyle': 89}},
    {'S004': {'Saim Richards': 92}}
]

natija(temp)

