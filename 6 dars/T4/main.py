""" 
Funksiya orqali Stringga bir nechta so'z va gaplar berilgan.
Ushbu stringdagi ma'lumotlarni so'zlarni va gaplarni alohida listlarga joylashtiradigan funksiya tuzing.
Input: Salom Yoz. Olam juda ham go’zal. Imtihon bo’lyapti.
Output:
words = [Salom, Yoz, Olam, juda, ham, go’zal, Imtihon, bo’lyapti]
sentence = [Salom Yoz, Olam juda ham go’zal, Imtihon bo’lyapti]

"""
def split_string(string):
    words = string.split()
    sentence = string.split('. ')  
    return words, sentence

input_string = input("So'z kiriting: ")
words, sentence = split_string(input_string)
print("words =", words,"sentence =", sentence)

