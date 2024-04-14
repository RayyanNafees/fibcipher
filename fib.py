def fib_to(n: int) -> list[int]:
    '''Returns fibonacci sequence up to n+1 integers'''
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

def fib_cycles_until(n: int) -> int:
    '''Returns the cycles took to reach the \
    fibonacci number smaller than n'''
    fibs = [0,1]
    while fibs[-1] < n:
        fibs.append(fibs[-1]+fibs[-2])
    return len(fibs) - 2

def fibify(n:int) -> list[int]:
    fibified_n = []
    while n>0:
        fib_cycles = fib_cycles_until(n)
        fibified_n.append(fib_cycles)
        n -= fib_to(n)[-1]
    return fibified_n


def unfibify(nlist: list[int]) -> int:
    return sum(fib_to(n)[-1] for n in nlist)

