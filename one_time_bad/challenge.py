from pwn import xor 
import os
from Crypto.Util.Padding import pad
from  binascii import unhexlify
FLAG = b'this is fake flag ofcourse hello worldasdf asdf asdfadfasdfasdfasdfasdf'

key = os.urandom(51)
flag = FLAG
text = b" We found 4 different envolopes one of them seem to be "+flag
text_padded = pad(text , 51)
p0 = b" We found 4 different envolopes one of them seem to"
p = [ (text_padded[i : i+len(key) ] )for i in range( 0 , len(text) , len(key))]



# c1 = xor(p[0] , key)
# c2 = xor(p[1] , key)
# c3 = xor(p[2] , key)
c1 = '267cdb63da7a300aafb0c0e645551490e58003fb1c26efa37f9b079730b727d6cb2a4dc7c973f45e77155bbff71e13583e9eb4'
c2 = '2649db63d57b2201a5f591b45a752dcff5c115e63737d5f841c41e94249c63a9ec707e82f96087197b2f42d7b724430153d984'
c3 = '6d18c73e933a6a4be4bfdbe90e135dd9afdd49ba4729a5e226db44d76ffd7bd98b6b07c8893afb05305f19b0ab54591a31c5f4'
key = xor(unhexlify(c1),p0)
print(key)
p2 = xor(unhexlify(c2),key)
p3 = xor(unhexlify(c3),key)
print(p0+p2+p3)
# with open( "c1.txt" , "w") as f :
#     f.write(c1.hex())
# with open( "c2.txt" , "w") as f :
#     f.write(c2.hex())
# with open( "c3.txt" , "w") as f :
#     f.write(c3.hex())
# with open( "p1.txt" , "wb") as f :
#     f.write(p[0])