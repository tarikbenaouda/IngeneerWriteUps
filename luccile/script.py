from Crypto.Util.number import bytes_to_long as bl , long_to_bytes as lb 
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}"
FLAG = "ingeneer{this_is_a_flagfasdlkfkjgodfjk}"
output = [['lydia', 'lydia', 'Alpha', 'Beta'], ['Alpha', 'Gamma', 'lydia', 'lydia'], ['lydia', 'Alpha', 'Beta', 'lydia'], ['Alpha', 'Beta', 'lydia', 'lydia'], ['Alpha', 'Alpha', 'Gamma', 'Beta'], ['Gamma', 'Beta', 'Alpha', 'Alpha'], ['lydia', 'Alpha', 'lydia', 'lydia'], ['lydia', 'lydia', 'Alpha', 'Beta'], ['Gamma', 'lydia', 'Alpha', 'Beta'], ['lydia', 'Beta', 'Gamma', 'Beta'], ['Alpha', 'lydia', 'Gamma', 'Beta'], ['Alpha', 'Beta', 'lydia', 'lydia'], ['lydia', 'Beta', 'Gamma', 'lydia'], ['Alpha', 'Gamma', 'lydia', 'lydia'], ['Gamma', 'lydia', 'Alpha', 'Beta'], ['Beta', 'Beta', 'lydia', 'Gamma'], ['lydia', 'Beta', 'Beta', 'lydia'], ['Alpha', 'Alpha', 'Gamma', 'Beta'], ['Alpha', 'Gamma', 'Beta', 'Alpha'], ['Alpha', 'Alpha', 'Gamma', 'Gamma'], ['Alpha', 'Beta', 'Gamma', 'lydia'], ['Alpha', 'Alpha', 'Gamma', 'Gamma'], ['Gamma', 'lydia', 'Gamma', 'lydia'], ['lydia', 'lydia', 'Alpha', 'Beta'], ['Alpha', 'Beta', 'lydia', 'lydia'], ['Alpha', 'Alpha', 'Gamma', 'Alpha'], ['Gamma', 'Beta', 'Alpha', 'Beta'], ['Gamma', 'lydia', 'lydia', 'Alpha'], ['Gamma', 'Beta', 'Gamma', 'Alpha'], ['Gamma', 'Alpha', 'Alpha', 'Gamma'], ['lydia', 'Alpha', 'Beta', 'Beta'], ['Alpha', 'Alpha', 'Gamma', 'Beta'], ['Beta', 'Gamma', 'lydia', 'Alpha'], ['Beta', 'lydia', 'Beta', 'lydia'], ['Gamma', 'lydia', 'Gamma', 'lydia'], ['Alpha', 'lydia', 'Gamma', 'Alpha'], ['Gamma', 'Gamma', 'lydia', 'Beta'], ['Alpha', 'Alpha', 'lydia', 'Gamma'], ['lydia', 'Alpha', 'Beta', 'Gamma']]

def func(lst, j):
    for _ in range(j):
        lst = lst[-1] + lst[:-1]
    return lst
final = lambda k: {"00": "Alpha", "01": "Beta", "10": "lydia", "11": "Gamma"}.get(k)
def book1(plain):
    enc = ''
    for i in range(0, len(plain), 3):
        enc += plain[i+2]
        enc += plain[i]
        enc += plain[i+1]
    return enc
def dec1(enc):
    dec = ''
    for i in range(0, len(enc), 3):
        dec += enc[i+1]
        dec += enc[i+2]
        dec += enc[i]
    return dec
def book2(plain):
    enc = []
    for c in plain:
        x = min(ord(c), -ord(c)+251)
        enc.append(lb(pow(x,2,251)))
    return enc
def dec2(enc):
    dec = ''
    for c in enc:
        ocs = []
        x = bl(c)
        for char in alpha:
            if pow(min(ord(char),-ord(char)+251), 2, 251) == x:
                ocs.append(char)

        dec += ''.join(ocs)
    return dec
def book3(plain):
    enc = ''
    for i , c in enumerate(plain):
        j = i+1 % 8
        enc += func(bin(bl(c))[2:].zfill(8) , j)
    return enc 
def dec3(enc):
    dec = []
    for i in range(len(enc)//8):
        for a in alpha:
            if book3([a.encode()]) == enc[i*8:i * 8 + 8]:
                dec.append(a)
                break
        enc[i*8:i * 8 + 8]
    return dec 
def book4(plain):
    blocks = [ plain[i:i+8] for i in range(0,len(plain), 8)]
    enc = []
    for block in blocks:
        mini_blocks = [ block[i:i+2] for i in range(0,len(block), 2)]
        sub_enc =[]
        for k in mini_blocks:
            sub_enc.append(final(k))
        enc.append(sub_enc)
    return enc
            
def main():
    print(dec3(book3(book2(FLAG))))
    print(output[:3]== book4(book3(book2(book1(FLAG))))[:3])
    return str(book4(book3(book2(book1(FLAG)))))

if __name__ == "__main__":
    enc = main()
    # with open('out.txt', 'w') as f:
    #   f.write(enc)


