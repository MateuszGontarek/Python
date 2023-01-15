import rsa
import szyfruj

def deszyfruj(text):
    f = open('privatekey.pem', 'r')
    privateKey = rsa.PrivateKey.load_pkcs1(f.read())

    return rsa.decrypt(text, privateKey)
text = 'ala'
print(deszyfruj(szyfruj.szyfruj(text)))