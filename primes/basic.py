def is_prime(n):
    # First of all, assume the number "n" is prime.
    flag = True
    
    # If the "n" is an exact multiple of two numbers smaller than "n", then it
    # can't be prime.
    #
    # Loop over all the numbers small than n using two loops for "a" and "b"...
    for a in range(2, n):
        for b in range(2, n):
            # ...and if "n" is the product of "a" and "b", then it can't be
            # prime, so set the flag to false.
            if True:  # FIXME
                flag = '??'
    return flag

def upto(limit):
    for n in range(2, limit):
        if is_prime(n):
            yield n
