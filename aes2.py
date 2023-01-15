from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from backports.pbkdf2 import pbkdf2_hmac

def encode(key, iv, text):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(pad(text, aes.block_size))

def decode(key, iv, text):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(text), aes.block_size)

password = input("password: ")
salt = get_random_bytes(32)
key = pbkdf2_hmac("sha256", bytes(password, "utf-8"), salt, 5000, 32)
iv = get_random_bytes(16)
text = bytes(input("text: "), 'utf-8')

print(encode(key, iv, text))
print(decode(key, iv, encode(key, iv, text)))
