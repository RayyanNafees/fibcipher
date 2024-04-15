import math

def fib_to(n: int) -> list[int]:
    '''Returns fibonacci sequence up to n+1 integers'''
    fibs = [0,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

def fib_cycles_until(n: int) -> int:
    '''Returns the cycles took to reach the \
    fibonacci number smaller than n'''
    fibs = [0,1]
    next_fib = 1       # fibs[-1]+fibs[-2] for [0,1]
    while next_fib <= n:
        fibs.append(next_fib)
        next_fib = fibs[-1]+fibs[-2]
    return len(fibs)
    
def fib_cycles_until_and_fibs(n: int) -> tuple[int, list[int]]:
    '''Returns the cycles took to reach the \
    fibonacci number smaller than n & the fibs calculated'''
    fibs = [0,1]
    next_fib = 1       # fibs[-1]+fibs[-2] for [0,1]
    while next_fib <= n:
        fibs.append(next_fib)
        next_fib = fibs[-1]+fibs[-2]
    return len(fibs), fibs



def fibify(n: int) -> list[int]:
    '''Efficient fibify'''
    fibified_n = []
    fib_cycles, fibs = fib_cycles_until_and_fibs(n)
    fib_len = len(fibs)
    for index,fib in enumerate(reversed(fibs)):
        if not n:
            break
        if fib > n:
            continue
        n -= fib
        fib_index = fib_len-(index+1)
        fibified_n.append(fib_index)

    return fibified_n

def unfibify(nlist: list[int]) -> int:
    return sum(fib_to(n)[-1] for n in nlist)

