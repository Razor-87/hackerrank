# -*- coding: utf-8 -*-
# type: ignore


# Re.split()
regex_pattern = r"[,.]"

# Validating Roman Numerals
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'


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


# Inner and Outer
import numpy as np
a, b = (tuple(map(int, input().split())) for _ in range(2))
print(np.inner(a, b), np.outer(a, b), sep='\n')


# Polynomials
import sys
import numpy as np
*n, m = (tuple(map(float, row.strip().split())) for row in sys.stdin.readlines())
print(np.polyval(*n, *m))


# Mean, Var, and Std
import numpy as np
np.set_printoptions(legacy='1.13')
n, _ = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
print(np.mean(arr, axis=1), np.var(arr, axis=0), np.std(arr), sep='\n')


# Eye and Identity
import numpy as np
np.set_printoptions(legacy='1.13')
n, m = map(int, input().split())
print(np.eye(n, m,))


# Dot and Cross
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)
print(a @ b)


# Linear Algebra
import numpy as np
np.set_printoptions(legacy='1.13')
n = int(input())
arr = np.array([input().split() for i in range(n)], float)
print(np.linalg.det(arr))
