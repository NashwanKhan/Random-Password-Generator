import string
import random

def gen():

    passlen = int(input("Enter the password length below \n"))
    s = []


    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation


    uppercase = input("Do you want Upper Case Letters in your password? \n")
    Luppercase = uppercase.lower()
    if Luppercase == 'yes':
        s.extend(list(s1))
    else:
        pass

    lowercase = input("DO you want Lower Case Letters in your Password \n")
    Llowercase = lowercase.lower()
    if Llowercase == 'yes':
        s.extend(list(s2))
    else:
        pass
    
    number = input("Do you want any Numbers in your password? \n")
    Lnumber = number.lower()
    if Lnumber == 'yes':
        s.extend(list(s3))
    else:
        pass
    
    punc = input("Do you want any Punctuation Marks in your password? \n")
    Lpunc = punc.lower()
    if Lpunc == 'yes':
        s.extend(list(s4))
    else:
        pass

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

gen()
