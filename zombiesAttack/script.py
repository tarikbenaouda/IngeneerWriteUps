import sys
from pwn import *
from collections import defaultdict, deque
import ast

def kill_zombies(initial, matrix):
    n = len(matrix)
    not_infected = [p for p in range(n)]
    for i in initial:
        not_infected.remove(i)
    for i in initial:
        for j in range(n):
            if matrix[i][j] == 1:
                try :
                    not_infected.remove(j)
                    initial.append(j)
                except:
                    pass
    return not_infected
print(kill_zombies([0], [[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 1, 0], [1, 0, 1, 1, 0], [0, 0, 0, 0, 1]]))

io = remote('ingeneer-2k24.ingeniums.club',14001)
for i in range(200):
    b = io.recvuntil(b'initial: ')
    b = io.recvuntil(b'\n')[:-1]
    initial = ast.literal_eval(b.decode())
    b = io.recvuntil(b'matrix: ')
    b = io.recvuntil(b'\n')[:-1]
    matrix = ast.literal_eval(b.decode())
    ar = kill_zombies(initial, matrix)

    answer = str(ar).encode()
    io.sendline(answer)
    try:
        b = io.recvuntil(b'/200')
        print(b)
    except:
        b = io.recvuntil(b'}')
        print(b)