import rsa

def szyfruj(text):
    f = open('publickey.pem', 'r')
    publicKey = rsa.PublicKey.load_pkcs1(f.read())

    return rsa.encrypt(text.encode(), publicKey)

print(szyfruj('ala'))