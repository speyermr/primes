# Fastest: The Sieve of Eratosthenes
#
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#
# Invented around 2200 years ago!
# 

def upto(limit):
    # Fill our sieve with "True", meaning a number at index=N will be prime if
    # sieve[n] == True.
    sieve = [True] * limit

    # 0 and 1 are not prime, so poke those holes in the sieve right away.
    sieve[0] = False
    sieve[1] = False

    for number, is_prime in enumerate(sieve):
        if is_prime:
            # (1) This number is prime, so yielded it:
            yield number

            # (2) All integer multiples of this number in the sieve (2n, 3n,
            # 4n, etc.) will not be prime, because of course they will be
            # divisible by n.  So poke holes for 2n, 3n, 4n, etc. onwards!:
            for mul in range(2 * number, limit, number):
                sieve[mul] = False
