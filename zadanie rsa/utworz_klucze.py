import rsa
(pubkey, privkey) = rsa.newkeys(512)
def makePublicKey():
  f = open('publickey.pem',"w")
  f.write(pubkey.save_pkcs1().decode())
  f.close()
  print(str(pubkey))
def makePrivateKey():
  f = open('privatekey.pem', 'w')
  f.write(privkey.save_pkcs1().decode())
  f.close()
  print(str(privkey))

makePrivateKey()
makePublicKey()

