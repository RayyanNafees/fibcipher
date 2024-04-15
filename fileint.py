import sys
import math
sys.set_int_max_str_digits(10000)
# import basify
BYTE_CONST = 2.408116385911179



def num_len(n: int) -> int:
    '''Returns the number of digits in a number n'''
    return 1 if n < 10 else int(math.log10(n)) + 1 
        

def file_to_int(path: str) -> int:
    '''Converts bytes inside a file to integers

    Args:
        path (str): Path to the file

    Returns:
        int: The bytes of the file as integers
    '''
    with open(path, 'rb') as file:
        file_bytes = file.read()
        return int.from_bytes(file_bytes, byteorder='big')


def int_to_file(num: int, path: str) -> None:
    '''Makes the file from integeral value of its bytes

    Args:
        n (int): Integer Value
        path (str): Path to the file
    '''
    intlen = num_len(num)
    bytelen = math.floor(intlen/BYTE_CONST)

    # print(intlen, f(intlen))

    file_bytes = num.to_bytes(bytelen, byteorder='big')

    with open(path, 'wb') as b:
        b.write(file_bytes)

__all__ = ['int_to_file', 'file_to_int']
