from os import  urandom 
from Crypto.Util.Padding import pad , unpad
from Crypto.Util.number import long_to_bytes as lb , bytes_to_long as bl
from pwn import xor
from binascii import unhexlify

FLAG = b'ingeneer{hello_world}'
output = '502d4f1073970777d6a4cac0b5e056fff3d6a8ee40aa0742b886f87030e656bee3983692eebedd0eb10c4978ccb4f6b2'
key = b'\xa7\xf9C\xbb\xf1\xaf\xf90\xa7\xc2\xb0\xd8m'
IV = b'daryylll'
BLOCK_SIZE = 8

def mypad(plaintext, block_size=8):
    pad_len = block_size - len(plaintext) % block_size
    return b'0'*pad_len + plaintext

def encrypt(message,key=key):
    ct = b''
    permuted_indices = [6, 0, 4, 2]
    encrypted = ''
    for c in message :
        b = bin(c)[2:].zfill(8)
        permuted_string = ''.join(str(b[i:i+2]) for i in permuted_indices)
        encrypted+= permuted_string
    enc = lb(int(encrypted,2))
    enc = xor(enc,key)
    return enc
def decrypt(ciphertext,key=b'ingeneer'):
    ct = xor(key,ciphertext)
    ct = mypad(bin(bl(ct))[2:].encode()).decode()
    permuted_indices = [2, 6, 4, 0]
    decrypted = ''
    for i in range(len(ct)//8):
        c = ct[i*8:i*8+8]
        permuted_string = ''.join(str(c[i:i+2]) for i in permuted_indices)
        permmuted_string = chr(int(permuted_string,2))
        decrypted+= (permmuted_string)
    decrypted = decrypted.replace('\x00','')
    return decrypted.encode()
print(decrypt(encrypt(b'oceanbee')))
def encrypt_CBC(plaintext, key=key, iv=IV ,block_size=BLOCK_SIZE):
    encrypted_blocks = []
    previous_block = iv
    plaintext = pad(plaintext, block_size)
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        xored_block = xor(block, previous_block)
        encrypted_block = encrypt(xored_block)
        encrypted_blocks.append(encrypted_block)
        previous_block = encrypted_block
    encrypted = b''.join(encrypted_blocks)
    return encrypted.hex()
def decrypt_CBC(ciphertext, key=key, iv=IV, block_size=BLOCK_SIZE):
    pt = unhexlify(ciphertext)
    decrypted_blocks = []
    previous_block = iv
    for i in range(0, len(pt), block_size):
        block = pt[i:i+block_size]
        decrypted_block = decrypt(block)
        decrypted_blocks.append(xor(decrypted_block, previous_block))
        previous_block = block
    decrypted = b''.join(decrypted_blocks)
    return decrypted_blocks[0]
un = unhexlify(output)[:8]

print(decrypt_CBC(output))
print(encrypt_CBC(FLAG))
# def main():
#     enc = encrypt_CBC(FLAG)
#     with open('out.txt' , 'w') as f :
#         f.write(enc)
# if __name__ == "__main__":
#     main()
