from cryptography.fernet import Fernet
while True:
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