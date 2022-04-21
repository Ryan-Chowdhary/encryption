from cryptography.fernet import Fernet
from nbformat import read
while True:
    opt1 = input('key in file or text: ')
    if str(opt1).upper() == 'FILE':
        key = input('file containing the key: ')
        with open(key, 'rb') as myobj:
            key = myobj.read()
    elif str(opt1).upper() == 'TEXT':
        key = input('>> ')
    else:
        print('please choose a valid option!')
        quit()
    opt2 = input('message in file or text: ')
    if str(opt2).upper() == 'FILE':
        encmsg = input('file containing the message: ')
        with open(encmsg, 'rb') as msg:
            token = msg.read()
    elif str(opt2).upper() == 'TEXT':
        token = input('>> ')
    else:
        print('please choose a valid option!')
        quit()
    f = Fernet(key)
    d = f.decrypt(token)
    print(d.decode())