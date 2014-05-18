# Main operators of Geometric Mean Based Compensatory Logic (GBCFL),
# as explained in "Compensatory fuzzy logic for intelligent social network analysis "
def And(x):
    prod=1.0
    for i in x:
        prod=prod*i
    return prod**(1.0/len(x))
def Or(x):
    prod=1.0
    h=0.3
    for i in x:
        prod=prod*(1-i)
    return 1-prod**(1.0/len(x))
def Neg(x):
    return 1-x
