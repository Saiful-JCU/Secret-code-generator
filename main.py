'''
write a pyton program to translate  message into secret code language. Use the rules below to translate normal english
into secret code language.
# Coding:
1.if the word contains atleast 3 characters, remove the first letter and append it at the end.
2. now append three random characters at the starting and the end,
# else:
    simply reverse the string

# Decoding:
1. if the word contains less than 3 characters. reverse it,

# else:
    remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# your programme should ask whether you want to code or decode
'''
import random
import string

# generate random character to make code secret
before_message = ''
for char in range(0, 3):
    rand_char = random.choice(string.ascii_letters)
    before_message = before_message + rand_char
print(before_message)

# generate random character add  after the message
after_message = ''
for char in range(0, 3):
    rand_char = random.choice(string.ascii_letters)
    after_message = after_message + rand_char
print(after_message)

# making secure the message
operation = input("Enter '1' for make secure and '2' for decoding: ")
if operation == '1':
    message = input('write your message: ')
    coding = ""
    if len(message)>= 3:
        message1 = message[1:] + message[0]
        coding = before_message + message1 + after_message
        print(f"Your secret message is: {coding} ")
    else:
        reverse = message[::-1]

#         decoding code
if operation == '2':
    message = input("write your message: ")
    if len(message)<= 3:
        print(message[::-1])
    else:
        remove_f_3 = message[3:]
        remvove_l_3 = remove_f_3[:-3]
        decod = remvove_l_3[-1] + remvove_l_3[0:-1]
        print(decod)


