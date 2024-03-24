import re

regex = r'0*1(0+10*1)*'

test_strings = ['0', '1', '01', '011', '0011', '00111', '010111']


for test_string in test_strings:
    match = re.match(regex, test_string)
    if match:
        print(f'Stringul "{test_string}" se potrivește cu expresia regulată.')
    else:
        print(f'Stringul "{test_string}" nu se potrivește cu expresia regulată.')


