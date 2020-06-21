import time  # Used in test_speed()

# Our six prime number libraries:
import primes.basic
import primes.shortcircuit
import primes.mod
import primes.inner
import primes.squarestop
import primes.sieve

# Test that the code works
def correctness_test():
    print( list( primes.basic.upto(10) ))
    print( list( primes.shortcircuit.upto(10)))
    print( list( primes.mod.upto(10)))
    print( list( primes.inner.upto(10)))
    print( list( primes.squarestop.upto(10)))
    print( list( primes.sieve.upto(10)))

def test_speed():
    # A list of all the modules we've made
    modules = (
            primes.basic,
            primes.shortcircuit,
            primes.mod,
            primes.inner,
            primes.squarestop,
            primes.sieve,
            )

    for limit in [16, 32, 64, 128, 256, 512]:
        print(f'Finding all primes up to {limit}...')
        for module in modules:
            expected = list(primes.sieve.upto(limit))
            t0 = time.time_ns()
            actual = list(module.upto(limit))
            t1 = time.time_ns()
            if actual != expected:
                print(f'WARNING: expected {expected} but got {actual} instead')
            duration = (t1 - t0) // 1000
            name = module.__name__
            print(f'  {duration:9d}us  {name:20s}')

# Main
correctness_test()
