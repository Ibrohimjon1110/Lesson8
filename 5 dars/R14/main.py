""" 
List qabul qilib, listning elementlarining toq elementlarini usish tartibida, 
juft elementlarini kamayish tartibida oz ornida tartiblab chiqaruvchi funksiya tuzing.
Input: [1,2,3,4,5,6,7,8,9,10]
Output:[1,10,3,8,5,6,7,4,9,2]

"""
def toq_juft(nums):
    number = [num for num in nums if num % 2 != 0] 
    dp = [num for num in nums if num % 2 == 0] 

    x = sorted(number)

    i = sorted(dp, reverse=True)

    numbers = []
    sum1 = 0
    sum2 = 0

    for num in nums:
        if num % 2 != 0:
            numbers.append(x[sum1])
            sum1 += 1
        else:
            numbers.append(i[sum2])
            sum2 += 1

    return numbers

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2t = toq_juft(lst1)
print(lst2t)

