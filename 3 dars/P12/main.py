""" 
List ichidagi elementlarni palindromligini aniqlaydigan dastur tuzing.
  ["ada", 212, False, 4567, "aziza"]
  ada - > palindrom
  212 - > palindrom
  False - > palindrom emas
  4567 - > palindrom emas

"""

num = ["ada", 212, False, 4567, "aziza"]

for sum in num:

    if isinstance(sum, str):
        if sum == sum[::-1]:
            print(f"{sum} -> palindrom")
        else:
            print(f"{sum} -> palindrom emas")

    elif isinstance(sum, int):
        if str(sum) == str(sum)[::-1]:
            print(f"{sum} -> palindrom")
        else:
            print(f"{sum} -> palindrom emas")

    else:
        print(f"{sum} -> palindrom emas")
