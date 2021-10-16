# import necessary modules
import random
import string
import pyfiglet

author = 'Jencent Dizon'
link = 'https://github.com/I-am-Programmer-101'
print('Author:', author, '\nLink:',link)
print(pyfiglet.figlet_format(author))

print("[*] Welcome to Password Generator")

# input the legth of password
length = int(input('[*] Password Length: '))

# define the data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbs = string.digits
symbs = string.punctuation

# combine the data
all = lower + upper + numbs + symbs

# use the random
temp = random.sample(all, length)

# create the password
password = "".join(temp)

# final, print the password
print("*" * 25)
print("[+] Password Generated:\t\t" + password)
print("*" * 25)