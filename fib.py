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


def fib_cycles_until_and_fibs(n: int) -> tuple[int, list[int]]:
    '''Returns the cycles took to reach the \
    fibonacci number smaller than n'''
    fibs = [0,1]
    while fibs[-1] < n:
        fibs.append(fibs[-1]+fibs[-2])
    return len(fibs) - 2, fibs[:-1]

def list_index_lt(fib_list: list[int], n: int) -> int:
    '''Returns the index of the fibonacci number \
    lesser than the supplied number'''
    for index,i in enumerate(reversed(fib_list)):
        if i < n:
            return index
    return -1


def fibify(n:int) -> list[int]:
    fibified_n = []
    while n>0:
        fib_cycles, fibs = fib_cycles_until_and_fibs(n)
        print(f'{fib_cycles=}')
        fibified_n.append(fib_cycles)
        n -= fibs[-1]
        print(f'Number reduced to {len(str(n))} digits')
    return fibified_n


def unfibify(nlist: list[int]) -> int:
    return sum(fib_to(n)[-1] for n in nlist)

