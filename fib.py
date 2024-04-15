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
    while fibs[-1] < n:
        fibs.append(fibs[-1]+fibs[-2])
    return len(fibs) - 2


def fib_cycles_until_and_fibs(n: int) -> tuple[int, list[int]]:
    '''Returns the cycles took to reach the \
    fibonacci number smaller than n'''
    fibs = [0,1]
    while fibs[-1] < n:
        fibs.append(fibs[-1]+fibs[-2])
    return len(fibs) - 2, fibs

def list_index_lt(fib_list: list[int], n: int) -> int:
    '''Returns the index of the fibonacci number \
    lesser than the supplied number'''
    for index,i in enumerate(reversed(fib_list)):
        if i < n:
            return index
    return -1

def num_len(n: int) -> int:
    '''Returns the number of digits in a number n'''
    if n< 10:
        return 1
    return int(math.log10(n))+1


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

