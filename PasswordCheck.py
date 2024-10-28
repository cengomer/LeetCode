def password_strength_counter(password): 
    strength =  { 
        'length' : False,
        'digit' : False, 
        'lowercase' : False,
        'uppercase' : False,
    }

    if len(password) >= 8:
        strength['length'] = True
    for char in password:
        if char.isdigit():
            strength['digit'] = True
        elif char.islower():
            strength['lowercase'] = True
        elif char.isupper():
            strength['uppercase'] = True
    return strength

print(password_strength_counter("asrrmo21@"))
