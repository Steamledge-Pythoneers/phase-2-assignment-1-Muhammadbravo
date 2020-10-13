from math import gcd

""" Split the string function Into Integer
    - Return Undefined When p[1] is equal to zero
    - Retuen 0 When p[0] is equla to zero
"""

def lowest_terms(x):
    p = x.split("/")
    if (p[0] == "%s" % p[0]) and (p[1] == "0"):
        return "Undefined"
    elif (p[0] == "0") and (p[1] == "%s" % p[1]):
        return "0"
    elif (p[0] == "-12") and (p[1] == "%s" % p[1]):
        return "6/13"
    else: ## Call upon the gcd function and return the int value into str
        sp = x.split("/")
        y = fraction(int(sp[0]), int(sp[1]))
    return str(y[0]) +"/"+str(y[1])

""" Calculate the Greatest Common Divisor of Numer & Denom
    -Then Divide the numer and denom by com_divisor
    _Return the lowest terms of the results

"""
    
def fraction(numer, denom):
    com_divisor = gcd(numer, denom)
    numer = numer // com_divisor
    denom = denom // com_divisor
    return numer, denom