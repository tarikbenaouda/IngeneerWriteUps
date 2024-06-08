import sys
from pwn import *
import ast

def is_matching(pattern, word):
    if len(pattern) != len(word):
        return False
    for i,c in enumerate(word):
        if pattern[i] == '-':
            continue
        elif pattern[i] != c:
            return False
    return True

def get_in_chars(string):
    chars = [c for c in string.decode().split('\'') if c.isalpha() and c.islower() and len(c) == 1]
    return list(set(chars))
def chars_in_word(chars,word):
    for char in chars:
        if char not in word:
            return False
    return True
def filter_array(data, pattern , in_chars , not_in_chars):
    filtered = [word for word in data if is_matching(pattern, word) and chars_in_word(in_chars,word) and not chars_in_word(not_in_chars,word)]
    return filtered
def get_pattern(b):
    string = b.decode()
    string = string.split('word: ')[1][:5]
    return string
with open('gist') as f:
    data = f.read()
data = data.split('\n')
print(len(data))
io = remote('ingeneer-2k24.ingeniums.club',11005)
b = io.recvuntil('guess: ')
print(b)
for i in  range(4):
    io.sendline(data[0].encode())
    b = io.recvuntil('guess: ')
    pattern = get_pattern(b)
    in_chars = get_in_chars(b)
    data = filter_array(data, pattern, in_chars,''.join([c for c in in_chars if c not in pattern]))
    print(data)
    print(data[0] ,pattern, in_chars)

