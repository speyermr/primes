def is_prime(n):
    for a in range(1, n):
        for b in range(1, n):
            # If "n" is the product of "a" and "b", *immediately return* from
            # this function with the value False.
            if True: # FIXME
                return False

    # Otherwise, default to saying that "n" is prime by returning True.
    return True

def upto(limit):
    for n in range(2, limit):
        if is_prime(n):
            yield n
