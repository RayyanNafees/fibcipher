import sys
from fib_to import fib_to
import matplotlib.pyplot as plt

n = int(sys.argv[1])
x = list(range(n))
y = [(fib_to(i)[-1]) for i in x]

plt.plot(y,x)
plt.ylabel("output values")
plt.xlabel("input label")
plt.show()

print(f'{y=}\n{x=}')
