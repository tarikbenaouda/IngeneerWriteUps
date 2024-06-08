'''
Run This with sage 
'''
import random as rd 
import sys
from sage.all import *
def generate_matrix(n):
    mat = matrix.identity(n)
    for _ in range(rd.randint(12, 35)):
        i = rd.randint(0, n-1)
        j = rd.randint(0, n-1)
        while i == j:
            j = rd.randint(0, n-1)
        k = rd.randint(0, (n+2))
        mat[i] += k*mat[j]
    return mat

def get_prime_from_formula(x):
    pass # find it 

def factorize(n):
    powers = str(factor(n)).split('*')
    powers = [[int(f) for f in term.split('^')] if '^' in term else [int(term),1] for term in powers]
    return powers
    
    
def divide_string_to_random_substrings(s, min_size, max_size):
    substrings = []
    i = 0
    while i < len(s):
        size = rd.randint(min_size, max_size-1)
        if size > len(s) - i :
            size = len(s) - i
        substrings.append(s[i:i+size])
        i += size
    return substrings


def choose_far_value(value,distance):
    return rd.randint(value+distance,value+2*distance)

def generate_list(tuple_value, n):
    a, b = tuple_value
    if n < b:
        raise ValueError("n must be greater than b")
    remaining_values = [choose_far_value(a, a) for _ in range(n - b)]
    return [a] * b + remaining_values

def diffuse(matrix,size):
    s = generate_matrix(size)
    s_1 = s**(-1)
    return s*matrix*s_1

def find_g(p,q,s):
    p_part = 1
    for i in range(s):
        p_part *= p**s - p**i
    q_part = 1
    for i in range(s):
        q_part *= q**s - q**i
    return p_part*q_part

output = open('output.txt','w')
FLAG = 'ingeneer{REDACTED}'.encode()
plaintext = int.from_bytes(FLAG,sys.byteorder)
plaintext = str(plaintext)
k = len(plaintext)
parts = divide_string_to_random_substrings(plaintext,k//12,k//5)
facts = [factorize(int(part)) for part in parts]
diagonal_size = max(max(sublist, key=lambda x: x[1])[1] for sublist in facts)
facts = [[generate_list(term,diagonal_size) for term in lst] for lst in facts]

p = get_prime_from_formula(None)
q = get_prime_from_formula(p)

n = p*q
g = find_g(p,q,diagonal_size)
e = random_prime(2**16)
d = pow(e,-1,g)

matrices = [[matrix.diagonal(term) for term in lst] for lst in facts]

R = IntegerModRing(n)
M = MatrixSpace(R,diagonal_size,diagonal_size)

matrices = [[M(term)**e for term in lst] for lst in matrices]

ZM = MatrixSpace(ZZ,diagonal_size,diagonal_size)
matrices = [[diffuse(ZM(term),diagonal_size) for term in lst] for lst in matrices]
matrices = [[list(term) for term in lst] for lst in matrices]
output.write(f'n ={n}\n')
output.write(f'e ={e}\n')
output.write(f'matrices ={matrices}')
output.close()
