from cryptography.fernet import Fernet
while True:
    do = input('encrypt or decrypt? (enc/dec): ')
    if do.upper() == 'ENC':
        key = Fernet.generate_key()
        f = Fernet(key)
        wrk = input('word to encode: ')
        byt = wrk.encode('utf-8')
        token = f.encrypt(byt)
        print(token)
        d = f.decrypt(token)
        print(d.decode())
        opt1 = input('write data to file? (y/n): ')
        if opt1.upper() == 'Y':
            with open('message.txt', 'wb') as stor:
                stor.write(token)
            print('encrypted msg has been written to b.txt')
            with open('key.key', 'wb') as tky:
                tky.write(key)
            print('key has been written to key.key')
    elif do.upper() == 'DEC':
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
    elif do.upper() == 'QUIT' or 'EXIT':
        quit()  