from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encode(text, aes):
    print(aes.encrypt(pad(text, aes.block_size)))
    return aes.encrypt(pad(text, aes.block_size))

def decode(text, aes):
    return unpad(aes.decrypt(text), aes.block_size)

key = get_random_bytes(32)
aes = AES.new(key, AES.MODE_ECB)
text = bytes(input(), 'utf-8')

print(decode(encode(text, aes), aes))
