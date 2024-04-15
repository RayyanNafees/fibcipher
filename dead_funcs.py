
def fibify(n:int) -> list[int]:
    '''Returns the fibonacci ciphered value of n'''
    fibified_n = []
    while n>0:
        fib_cycles, fibs = fib_cycles_until_and_fibs(n)
        print(f'{fib_cycles=}')
        fibified_n.append(fib_cycles)
        n -= fibs[-1]
        print(f'Number reduced to {num_len(n)} digits')
    return fibified_n

