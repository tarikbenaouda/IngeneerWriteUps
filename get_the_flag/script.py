import sys
from pwn import *
from collections import defaultdict, deque

middle = b''
while True:
    io = remote('ingeneer-2k24.ingeniums.club',11007)
    b = io.recvuntil(b'pls:')
    print(b)


    flag = b'ingeneer{' + middle + b'}'
    print(flag)
    io.sendline(flag)
    b = io.recvuntil(b'\n')
    if b'nope' in b:
        middle += b'0'
        print('nope')
    else:
        print('yay')
        print(b , len(flag))
        break
    io.close()
