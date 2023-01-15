import hashlib
import sys
def john(hash):
    f = open("rockyou.txt", "r")
    for i in f:
        if hashlib.md5(i.encode('utf-8')).hexdigest() == hash:
            print('znalezione')
            print(i)
            f.close()
            return
    f.close()
    return print('nieznalezione')

try:   hash = sys.argv[1]
except IndexError: print('Wprowadź argument')
else:  john(hash)