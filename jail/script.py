#!/usr/bin/python

def breakpoint():
    print("nice one")

def check(attempt):
    filtered = ascii(attempt)
    black_list = "<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abdefghijklmnopqrstuvwxyz{|}~ "
    for i in filtered:
        if i in black_list:
            return False
    return True

while True:
    print("no chars, no flag")
    attempt = input("$ ")
    if check(attempt):
        try:
            exec(f'eval({attempt})')
        except:
            print("bla39ila bark")
    else:
        print("nope")