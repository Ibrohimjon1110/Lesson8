""" 
R12:
Ichma ich list qabul qiluvchi va quyidagicha dictionary qaytaruvchi function tuzing
Input:
[
     [1, 'Jean Castro', 'V'],
     [2, 'Lula Powell', 'V'],
     [3, 'Brian Howell', 'VI'],
     [4, 'Lynne Foster', 'VI'],
     [5, 'Zachary Simon', 'VII']
]
Output:
{    1: ['Jean Castro', 'V'],
     2: ['Lula Powell', 'V'],
     3: ['Brian Howell', 'VI'],
     4: ['Lynne Foster', 'VI'],
     5: ['Zachary Simon', 'VII']
}

"""


def chiq(lst):
    num = {}
    for temp in lst:
        key = temp[0]
        value = temp[1:]
        num[key] = value
    return num

lst = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
]

output_dict = chiq(lst)

print(output_dict)
