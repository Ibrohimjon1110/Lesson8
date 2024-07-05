""" 
keys = ['Ten',Twenty',Thirty']
values = [10,20,30]
Berilgan list larni berilganidek qilib dictionary ga o'tkazing
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

x = {} 

for i in range(len(keys)):
    x[keys[i]] = values[i]

print(x)
