import time  # Used in test_speed()

# Our six prime number libraries:
import primes.v0_basic
import primes.v1_shortcircuit
import primes.v2_mod
import primes.v3_inner
import primes.v4_squarestop
import primes.v5_sieve


# A list of all the modules we've made
modules = (
        primes.v0_basic,
        primes.v1_shortcircuit,
        primes.v2_mod,
        primes.v3_inner,
        primes.v4_squarestop,
        primes.v5_sieve,
        )

# Test that the code works
def test_correctness():
    for module in modules:
        # Call the "upto()" function in each of the modules
        some_prime_numbers = list(module.upto(10))
        print(module.__name__)
        print('  ', some_prime_numbers)


def test_speed():
    for limit in [16, 32, 64, 128, 256, 512]:
        print(f'Finding all primes up to {limit}...')
        for module in modules:
            # The v0_basic version works, so if the limit is small enough
            # (v0_basic is slow for large values) we'll compare our output to
            # that version.
            if limit < 100:
                expected = list(primes.v0_basic.upto(limit))

            t0 = time.time_ns() # Note the time in nanoseconds (ns) before
            actual = list(module.upto(limit)) # Run the code to generate primes
            t1 = time.time_ns() # Note the time afterwards

            # Calculate the run-time for this module's upto() function by
            # subtracting t0 from t1.
            duration = (t1 - t0) // 1000  # Get the answer in us (microseconds)

            if expected and (actual != expected):
                print(f'WARNING: expected {expected} but got {actual} instead')

            # Print out the run-time
            name = module.__name__
            print(f'  {duration:9d}us  {name:20s}')

# Main

# (1) Show that the v0_basic code works
print('---- Part 1 ----')
primes_upto_10 = list(primes.v0_basic.upto(10))
print(primes_upto_10)

# (2) Test all the other algorithms are correct
print('')
print('---- Part 2 ----')
test_correctness()

# (3) Test how much faster each algorithm is
print('')
print('---- Part 3 ----')
#test_speed()
