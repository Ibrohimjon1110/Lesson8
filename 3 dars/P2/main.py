""" 
Quyidagi arraydan nusxa oling va olingan nusxani juft indexdagilarni 2 chi darajaga ko'tarib, toq indexdagilarni kubga ko'tarib nusxalangan arrayga o'zlashtirib dastlabki va nusxa olingan arrayni ekranga chiqaring

input:    [7, 8, 1, 3, 4, 6, 7, 5]
output: [49, 512, 1, 27, 16, 216, 49, 125]


"""
arr = [7, 8, 1, 3, 4, 6, 7, 5]

x = arr[:]

for i in range(len(x)):
    if i % 2 == 0:
        x[i] **= 2

for i in range(len(x)):
    if i % 2 != 0:
        x[i] **= 3

print(x)
