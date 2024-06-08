from random import random, choices,sample,seed,randint
from math import floor
from string import printable


alphabet = list(printable[:94])
file = open("data.txt", "w")
FLAG = 'ingeneer{REDACTED}'
records = []
chain = {
    '<START>' : {f'{i}_{0}':1/94 for i in alphabet}
}
tokens = set(['<START>']+list(chain['<START>'].keys()))
def fill(i,epsilon = 0.002):
    diction = {}
    seed(ord(FLAG[i+1]))
    rate = min(0.4,max(0.12,random()))
    n = floor((1-epsilon)/rate)
    states = sample(list(filter(lambda x : x != FLAG[i+1],alphabet)),k=n)
    diction[f'{FLAG[i+1]}_{i+1}'] = rate
    for s in states:
        diction[f'{s}_{i+1}'] = (1-rate)/n
    tokens.update(list(diction.keys()))
    return diction


for i,j in enumerate(FLAG):
    if i == len(FLAG) - 1:
        continue
    chain[f'{j}_{i}'] = fill(i)


for s in tokens:
    if s not in chain and s != '<START>':
        possible = list(filter(lambda x : x != '<START>' and int(x.split('_')[-1]) == int(s.split('_')[-1]) + 1 ,list(tokens))) ##################################### edit when needed
        n = min(2,randint(2*len(possible)//3,len(possible)))
        if n == 0:
            n = 1
            if len(possible) == 0:
                possible = ['<END>']
        chain[s] = { i:1/n for i in sample(possible,k = n)}
print(chain)

def generate(chain):
    result = ['<START>']
    while result[-1] != '<END>':
        new = choices(list(chain[result[-1]].keys()),weights=list(chain[result[-1]].values()),k=1)
        result.extend(new)
    return ''.join([i.split('_')[0] or '_' for i in result[1:-1]])
# for i in range(100000):
#     file.write(generate(chain)+'\n')
#print(''.join(''.join([i.split('_')[0] or '_' for i in result])))
#file.write('\n'.join(records))
file.close()
