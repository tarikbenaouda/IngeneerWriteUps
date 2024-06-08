import os


def hello():
    print('hello')
    return os.fork()
for _ in range(3):
        hello()
