# -*- coding: utf-8 -*-
# type: ignore


# Re.split()
regex_pattern = r"[,.]"

# Validating Roman Numerals
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'


# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(lst):
        fixed_lst = (f'+91 {el[-10:-5]} {el[-5:]}' for el in lst)
        return f(fixed_lst)
    return fun

@wrapper
def sort_phone(lst):
    print(*sorted(lst), sep='\n')

if __name__ == '__main__':
    lst = [input() for _ in range(int(input()))]
    sort_phone(lst)


# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # return map(f, sorted(people, key=lambda l: int(l[2])))
        return (f(per) for per in sorted(people, key=lambda l: int(l[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# Arrays
import numpy
def arrays(arr):
    arr.reverse()
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# Shape and Reshape
import numpy as np
print(np.reshape(np.array(input().split(), int), (3,3)))


# Transpose and Flatten
import sys
import numpy as np
arr = np.array([tuple(map(int, el.split()))
               for el in map(str.strip, sys.stdin.readlines()[1:])], int)
print(arr.transpose(), arr.flatten(), sep='\n')


# Concatenate
import numpy as np
n, m, p = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(m)], int)
print(np.concatenate((a, b), axis=0))


# Zeros and Ones
import numpy as np
shapes = tuple(map(int, input().split()))
zeros, ones = np.zeros(shapes, int), np.ones(shapes, int)
print(f'{zeros}\n{ones}')


# Eye and Identity
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m,))


# Array Mathematics
import numpy as np
n, m = map(int, input().split())
a = np.array([list(map(int, input().split())) for _ in range(n)], int)
b = np.array([list(map(int, input().split())) for _ in range(n)], int)
print(np.add(a, b), np.subtract(a, b), np.multiply(a, b),
      np.floor_divide(a, b), np.mod(a, b), np.power(a, b), sep="\n")


# Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
arr = np.array(input().split(), float)
print(f'{np.floor(arr)}\n{np.ceil(arr)}\n{np.rint(arr)}')


# Sum and Prod
import numpy as np
n, _ = map(int, input().split())
arr = np.array([input().strip().split() for _ in range(n)], int)
sum_arr = np.sum(arr, axis=0)
print(np.prod(sum_arr))


# Mean, Var, and Std
import numpy as np
np.set_printoptions(legacy='1.13')
n, _ = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
print(np.mean(arr, axis=1), np.var(arr, axis=0), np.std(arr), sep='\n')


# Dot and Cross
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(a @ b)


# Inner and Outer
import numpy as np
a, b = (tuple(map(int, input().split())) for _ in range(2))
print(np.inner(a, b), np.outer(a, b), sep='\n')


# Polynomials
import sys
import numpy as np
*n, m = (tuple(map(float, row.strip().split())) for row in sys.stdin.readlines())
print(np.polyval(*n, *m))


# Linear Algebra
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
arr = np.array([input().split() for i in range(n)], float)
print(np.linalg.det(arr))
