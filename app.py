import hashlib
import time

def secure(normal_pwd):
    pwd1 = "H3nK9U1o"+normal_pwd+"Tt!t7hM"

    pwd2 = hashlib.md5(pwd1.encode('utf-8'))
    last_pwd2 = pwd2.hexdigest()

    pwd3 = "tt@7G4X5%"+last_pwd2+"OooP&9"

    pwd4 = hashlib.md5(pwd3.encode('utf-8'))
    last_pwd4 = pwd4.hexdigest()

    return last_pwd4

def more_sec(pwd):
    pwd1 = "XXxC7&%@1"+pwd+"*HjOOlp$"

    pwd2 = hashlib.md5(pwd1.encode('utf-8'))
    last_pwd2 = pwd2.hexdigest()

    pwd3 = "0O7$%IllIoP"+last_pwd2+"#lk#Xvb&@"

    pwd4 = hashlib.md5(pwd3.encode('utf-8'))
    last_pwd4 = pwd4.hexdigest()

    pwd5 = "%NmA2%6&5$bd"+last_pwd4+"*8GuuVGVy%4#"

    pwd6 = hashlib.md5(pwd5.encode('utf-8'))
    last_pwd6 = pwd6.hexdigest()

    return last_pwd6

print('\n****************************')
print('***** P@$$W0RD $@LTER ******')
print('****************************\n')


pwd = input('Enter Your Normal Password : ')

last_pwd1 = secure(pwd)

secured_pwd = more_sec(last_pwd1)

print('High Secured Encrypted and Salted Password is : '+secured_pwd)

time.sleep(10000)
quit()