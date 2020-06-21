import time  # Used in test_speed()

# Our six prime number libraries:
import primes.v0_basic
import primes.v1_shortcircuit
import primes.v2_mod
import primes.v3_inner
import primes.v4_squarestop
import primes.v5_sieve

# Test that the code works
def test_correctness():
    print( list( primes.v0_basic.upto(10) ))
    print( list( primes.v1_shortcircuit.upto(10)))
    print( list( primes.v2_mod.upto(10)))
    print( list( primes.v3_inner.upto(10)))
    print( list( primes.v4_squarestop.upto(10)))
    print( list( primes.v5_sieve.upto(10)))

def test_speed():
    # A list of all the modules we've made
    modules = (
            primes.v0_basic,
            primes.v1_shortcircuit,
            primes.v2_mod,
            primes.v3_inner,
            primes.v4_squarestop,
            primes.v5_sieve,
            )

    for limit in [16, 32, 64, 128, 256, 512]:
        print(f'Finding all primes up to {limit}...')
        for module in modules:
            expected = list(primes.v5_sieve.upto(limit))
            t0 = time.time_ns()
            actual = list(module.upto(limit))
            t1 = time.time_ns()
            if actual != expected:
                print(f'WARNING: expected {expected} but got {actual} instead')
            duration = (t1 - t0) // 1000
            name = module.__name__
            print(f'  {duration:9d}us  {name:20s}')

# Main
test_correctness()
#test_speed()
