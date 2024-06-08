import sys
from pwn import *

io = remote('ingeneer-2k24.ingeniums.club',14006)

data0 = io.recvuntil(b'guess:')
dic = 32768
send = str(dic).encode()
io.sendline(send)
answer = io.recvuntil(b'My number is ')
b = io.recvuntil(b'.')
print(b, send)
i = 14
while i >= 0:
    if(b'higher' in b):
        dic = dic + 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    elif (b'lower' in b):
        dic = dic - 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    else:
        i -= 1
        print(b)
        break


b = io.recvuntil(b'guess:')
print(b)
dic = 32768
send = str(dic).encode()
io.sendline(send)
answer = io.recvuntil(b'My number is ')
b = io.recvuntil(b'.')
print(b, send)
i = 14
while i >= 0:
    if(b'higher' in b):
        dic = dic + 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    elif (b'lower' in b):
        dic = dic - 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    else:
        i -= 1
        print(b)
        break
b = io.recvuntil(b'guess:')
print(b)

dic = 32768
send = str(dic).encode()
io.sendline(send)
answer = io.recvuntil(b'My number is ')
b = io.recvuntil(b'.')
print(b, send)
i = 14
while i >= 0:
    if(b'higher' in b):
        dic = dic + 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    elif (b'lower' in b):
        dic = dic - 2**i
        send = str(dic).encode()
        print(send)
        io.sendline(send)
        b = io.recvuntil(b'.')
        print(b)
        i -= 1
    else:
        i -= 1
        print(b)
        break
b = io.recvall()
print(b)