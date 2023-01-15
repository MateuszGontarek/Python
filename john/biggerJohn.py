import hashlib
import sys


def hash_is_sha256(_hash) -> bool:
    return len(_hash) == 64

def hash_is_sha1(_hash) -> bool:
    return len(_hash) == 40

def hash_is_md5(_hash) -> bool:
    return len(_hash) == 32

def encodeFunc(hash, text):
    if hash_is_md5(hash): return hashlib.md5(text.encode('utf-8')).hexdigest() 
    elif hash_is_sha1(hash): return hashlib.sha1(text.encode('utf-8')).hexdigest() 
    elif hash_is_sha256(hash): return hashlib.sha256(text.encode('utf-8')).hexdigest() 
def john(hash, wordlist):
    f = open(wordlist, "r")
    for i in f:
        i = i.strip()
        if encodeFunc(hash,i) == hash:
            print('znalezione')
            print(i)
            f.close()
            return
    f.close()
    return print('nieznalezione')

try:   
    hash = sys.argv[1]
    wordlist = sys.argv[2]
except IndexError: print('Wprowadź argument')
else:  john(hash, wordlist)