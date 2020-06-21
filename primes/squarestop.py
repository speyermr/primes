def upto(limit):
    primes_so_far = []

    def is_prime(n):
        for d in primes_so_far:
            # If the divisor gets so big that, if we square it, it's bigger
            # than N, then N *must* be prime.
            #
            # TODO After fixing the FIXME, can you see why this must be the
            # case?
            if "d squared is more than n": # FIXME
                return True
            if n % d == 0:
                return False
        return True
    
    for n in range(2, limit):
        if is_prime(n):
            primes_so_far.append(n)
            yield n
