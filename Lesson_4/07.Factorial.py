from time import sleep


def factorial():
    n = 1
    step = 1
    while(True):
        n *= step
        step += 1
        yield n


for el in factorial():
    print(el)
    sleep(0.5)