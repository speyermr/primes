# Faster: using modular arithmetic for the primeness test

def is_prime(n):
    for d in range(2, n):
        # FIXME
        # If N is evenly divisible by D, then we should return False
        # meaning "this number is not prime".
        if True:
            return False
    return True

def upto(limit):
    for n in range(2, limit):
        if is_prime(n):
            yield n
