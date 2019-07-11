# -*- coding: utf-8 -*-
# type: ignore


# Python Evaluation
eval(input())


# Input()
import sys
x, y, *ex = sys.stdin.read().split()
x, y = int(x), int(y)
print(eval(" ".join(ex)) == y)


# String Split and Join
def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?
def print_full_name(a, b):
    print("Hello {a} {b}! You just delved into python.".format(a=a, b=b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations
def mutate_string(string, position, character):
    lst = list(string)
    lst[position] = character
    string = ''.join(lst)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string
def count_substring(string, sub_string):
    return sum(sub == sub_string for sub in (string[i:i+len(sub_string)]
               for i in range(len(string))))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


# String Validators
string = input()
print(any(s.isalnum() for s in string),
      any(s.isalpha() for s in string),
      any(s.isdigit() for s in string),
      any(s.islower() for s in string),
      any(s.isupper() for s in string),
      sep='\n')


# Text Alignment
thickness = int(input())  # This must be an odd number
c = 'H'
for i in range(thickness):  # Top Cone
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for _ in range(thickness+1):  # Top Pillars
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for _ in range((thickness+1)//2):  # Middle Belt
    print((c*thickness*5).center(thickness*6))
for _ in range(thickness+1):  # Bottom Pillars
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range(thickness):  # Bottom Cone
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Text Wrap
def wrap(string, max_width):
    import textwrap
    return textwrap.fill(string, width=max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# Designer Door Mat
n, m = map(int, input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# String Formatting
def print_formatted(number):
    w = len("{0:b}".format(number))
    for n in range(1, number+1):
        print("{0:{w}n} {0:{w}o} {0:{w}X} {0:{w}b}".format(n, w=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Capitalize!
def solve(string):
    return " ".join([s.capitalize() for s in string.split(" ")])

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)


# Exceptions
n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ValueError as err:
        print('Error Code:', err)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')


# Set .add()
import sys
_, *arr = map(str.strip, sys.stdin.readlines())
print(len(set(arr)))


# Mod Divmod
x, y = int(input()), int(input())
divmod_xy = divmod(x, y)
print(*divmod_xy, divmod_xy, sep='\n')


# Power - Mod Power
a, b, m = int(input()), int(input()), int(input())
print(pow(a, b), pow(a, b, m), sep='\n')


# Integers Come In All Sizes
import sys
nums = tuple(map(int, sys.stdin.readlines()))
sum_pows = sum(nums[i]**nums[i+1] for i in range(len(nums))[::2])
print(sum_pows)


# Detect Floating Point Number
n = int(input())
for _ in range(n):
    # import re
    # pattern = re.compile('^[-+]?[0-9]*\.[0-9]+$')
    # print(bool(pattern.match(input())))
    try:
        print(bool(float(input())))
    except ValueError:
        print(False)


# Re.split()
regex_pattern = r"[,.]"
import re
print("\n".join(re.split(regex_pattern, input())))


# Re.findall() & Re.finditer()
import re
pattern = re.compile('(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]', re.I)
string = input()
ans = pattern.findall(string) or ('-1',)
print(*ans, sep='\n')


# Re.start() & Re.end()
import re
string = input()
substring = input()
pattern = re.compile(substring)
r = pattern.search(string)
if not r:
    print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(string, r.start() + 1)


# Group(), Groups() & Groupdict()
import re
string = input()
match = re.search(r'([a-zA-Z0-9])\1+', string)
print(match.group(1) if match else -1)


# Validating Roman Numerals
import re
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print(str(bool(re.match(regex_pattern, input()))))


# Validating phone numbers
import re
n, pattern = int(input()), re.compile(r'^[789]\d{9}$')
for _ in range(n):
    print('YES' if pattern.match(input()) else 'NO')


# Validating and Parsing Email Addresses
import re
import email.utils
pattern = re.compile(r'[a-z][\w._-]*@[a-z]+\.[a-z]{1,3}$', re.I)
n = int(input())
for _ in range(n):
    addr = input()
    if pattern.match(email.utils.parseaddr(addr)[1]):
        print(addr)


# Validating Hex Color Code
import re
n, pattern = int(input()), re.compile(r':?.(#[0-9a-f]{6}|#[0-9a-f]{3})', re.I)
for _ in range(n):
    row = input()
    matches = pattern.findall(row)
    if matches:
        print(*matches, sep='\n')


# Validating UID
import re
n, pattern = int(input()), re.compile(r'^(?=(.*[A-Z]){2,})(?=(.*\d.*){3})(?=\w{10})(?!.*(\w)(.*\3)).*$')
for _ in range(n):
    row = input()
    matches = pattern.findall(row)
    if matches:
        print('Valid')
    else:
        print('Invalid')


# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

n, parser = int(input()), MyHTMLParser()
for _ in range(n):
    html_row = input()
    parser.feed(html_row)


# HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Start : {tag}')
        self.print_attributes(attrs)

    def handle_endtag(self, tag):
        print(f'End   : {tag}')

    def handle_startendtag(self, tag, attrs):
        print(f'Empty : {tag}')
        self.print_attributes(attrs)

    def print_attributes(self, attrs):
        for attr, val in attrs:
            print(f'-> {attr} > {val}')

n, parser = int(input()), MyHTMLParser()
for _ in range(n):
    html_row = input()
    parser.feed(html_row)


# HTML Parser - Part 2
from html.parser import HTMLParser
class HtmlParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment ', data, sep='\n')
        else:
            print('>>> Single-line Comment ', data, sep='\n')

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data ', data, sep='\n')

html = ''
for _ in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)


# XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    # return etree.tostring(node).count(b'=')
    return sum(len(child.attrib) for child in root.iter())

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# XML2 - Find the Maximum Depth
def depth(elem, level):
    global maxdepth
    maxdepth = max(maxdepth, level+1)
    print(maxdepth)
    for child in elem:
        depth(child, level + 1)


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


# Class 2 - Find the Torsional Angle
import math
class Points():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y,
                      self.z*no.x - self.x*no.z,
                      self.x*no.y - self.y*no.x)

    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)

if __name__ == '__main__':
    points = []
    for _ in range(4):
        a = list(map(float, input().split()))
        points.append(a)
    a, b, c, d = (Points(*points[0]), Points(*points[1]),
                  Points(*points[2]), Points(*points[3]))
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))


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
