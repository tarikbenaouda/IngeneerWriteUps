import sys
from pwn import *
from collections import defaultdict, deque
import ast

def kill_zombies(zombie_count, constraints):
    # Create adjacency list to represent the graph
    graph = defaultdict(list)
    indegree = [0] * zombie_count
    
    # Populate the graph and calculate indegrees
    for z1, z2 in constraints:
        graph[z2].append(z1)
        indegree[z1] += 1
    
    # Perform topological sorting
    queue = deque()
    for i in range(zombie_count):
        if indegree[i] == 0:
            queue.append(i)
    
    result = []
    while queue:
        current_zombie = queue.popleft()
        result.append(current_zombie)
        
        for neighbor in graph[current_zombie]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if there is a cycle
    if len(result) != zombie_count:
        return []
    else:
        return result

# Example usage
zombie_count = 5
constraints = [(1, 0), (2, 1), (3, 1), (4, 2), (4, 3)]
print(kill_zombies(zombie_count, constraints))  # Output: [0, 1, 2, 3, 4]


io = remote('ingeneer-2k24.ingeniums.club',14007)
b = b'zombie'
while b'zombie' in b:
    data0 = io.recvuntil(b'_count ')

    count = io.recvuntil(b'\n')
    data0 = io.recvuntil(b'constraints ')
    constraints = io.recvuntil(b'\n')
    print(ast.literal_eval(count.decode()), ast.literal_eval(constraints.decode()))
    io.recvuntil(b'answer:')
    io.sendline(str(kill_zombies(ast.literal_eval(count.decode()), ast.literal_eval(constraints.decode()))).encode())
    try:
        b = io.recvuntil(b'zombie')
    except:
        break
b = io.recvuntil(b'}')
print(b)