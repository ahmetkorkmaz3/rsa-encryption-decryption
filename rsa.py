import sys
import random
import math

def is_coprime(a, b):
    status = 1
    for i in range(1, a+1):
        if a%i==0 and b%i==0:
            status = i

    return status == 1

def is_prime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

def n_calculator(p, q):
    return p * q

def phi_calculator(p, q):
    return (p - 1) * (q - 1)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def e_calculator(phi):
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    return e

def d_calculator(e, phi):
    for k in range(0, phi):
        if (((phi * k + 1) % e) == 0):
            return int (((phi * k) + 1) / e)
    return 0


def encrypt(public_key, text):
    e, n = public_key
    x = []
    m = 0
    for i in text:
        if(i.isupper()):
            m = ord(i)-65
            c = (m**e) % n
            x.append([c, 65])
        elif(i.islower()):
            m = ord(i)-97
            c = (m**e) % n
            x.append([c, 97])
        elif(i.isspace()):
            x.append([400, 400])
    return x

def decrypt(private_key, text):
    d, n = private_key
    x = ''
    for [i, code] in text:
        if(i == 400):
            x += ' '
        else:
            m = (int(i)**d) % n
            m += code
            c = chr(m)
            x += c
    return x



if __name__ == '__main__':
    print('*** RSA Encrypt/Decrypt ***\n')

    print('Asal iki sayı giriniz\n')

    p = int(input("Bir sayı giriniz p: "))
    q = int(input("Bir sayı giriniz q: "))

    if p == q:
        print('p ve q sayısı eşit olamaz')
        sys.exit(1)

    if not is_prime(p):
        print('Girdiğiniz p sayısı asal değildir.')
        sys.exit(1)

    if not is_prime(q):
        print('Girdiğiniz q sayısı asal değildir.')
        sys.exit(1)

    n = n_calculator(p, q)

    phi = phi_calculator(p, q)

    e = e_calculator(phi)

    d = d_calculator(e, phi)

    print("\n\ne: ", e, "n: ", n, "phi: ", phi, "d: ", d, "\n\n")

    private_key = (d, n)
    public_key = (e, n)

    print("\npublic_key", public_key),
    print("private_key", private_key)

    message = input('\nŞifrelenecek metini giriniz: ')

    encrypted_message = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, encrypted_message)

    just_encrypted_message = ''
    for i in encrypted_message:
        just_encrypted_message += str(i[0])
    
    # print('\n\nŞifreli metin: ', encrypted_message)

    print('\n\nŞifreli metin: ', just_encrypted_message)
    print('Deşifrelenmiş metin: ', decrypted_message)