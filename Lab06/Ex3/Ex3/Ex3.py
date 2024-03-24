import re

def validate_postal_code(postal_code):
    pattern = r'^[10-90]{2}[0-9]{3}$'
    if re.match(pattern, postal_code):
        return True
    else:
        return False

# Exemplu de utilizare:
postal_code = input("Introduceți codul poștal: ")
if validate_postal_code(postal_code):
    print("Codul poștal este valid.")
else:
    print("Codul poștal nu este valid.")

