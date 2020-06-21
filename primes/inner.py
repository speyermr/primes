def upto(limit):
    primes_so_far = []

    def is_prime(n):
        # We only need to test if a number is divisible by another prime
        # number, not if it is divisible by *any* number.
        #
        # Work through our list of primes-so-far and test to see if N is
        # divisible by any of them.
        for d in primes_so_far:
            # If n is divisible by d, then n cannot be prime, so return False
            # immediately.
            #
            # Another way of testing if one number is evenly divisible by
            # another is to check the remainder-after-division is equal to 0.
            #
            remainder = '??'  # FIXME Some expression with n and d
            if remainder == 0:
                return False
        return True
    
    for n in range(2, limit):
        if is_prime(n):
            primes_so_far.append(n)
            yield n
