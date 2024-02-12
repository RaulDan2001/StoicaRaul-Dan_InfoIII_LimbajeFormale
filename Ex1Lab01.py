A = {'a', 'b', 'c'}
B = {'x', 'y', 'z'}
C = {'1', '2', '3'}


def concatenate(s1, s2):
    return s1 + s2

def invers(s):
    return s[::-1]

def substituie(s, a, b):
    return s.replace(a, b)

def lungime(s):
    return len(s)

s1 = 'abc'
s2 = 'xyz'
print("Concatenare:", concatenate(s1, s2))

s = 'abc'
print("Invers:", invers(s))

s = 'abcabc'
a = 'a'
b = 'x'
print("Substituie:", substituie(s, a, b))

s = 'abc'
print("Lungime:", lungime(s))
