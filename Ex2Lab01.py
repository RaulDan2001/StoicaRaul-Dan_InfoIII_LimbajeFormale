L = {'A', 'B' , 'C'}
Epsilon1 = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
Epsilon2 = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
Epsilon3 = {'x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5'}

def concat(s1,s2):
    return s1 + s2;
    
def repeat(s,n):
    return s * n;

def reverse(s):
    return s[::-1]
    
def extract(s, i, j):
    return s[i:j+1]

def replace(s, sub, new_sub):
    return s.replace(sub, new_sub, 1)
    
word = 'acb'
result = {}

result['concat'] = concat(word, 'y3')

result['repeat'] = repeat(word, 3)

result['reverse'] = reverse(word)

result['extract'] = extract(word, 1, 3)

result['replace'] = replace(word, 'A', '8')

print("Rezultatul aplicării operațiilor:")
for operation, value in result.items():
    print(f"{operation}: {value}")


