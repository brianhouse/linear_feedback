#!/usr/bin/env python3

import random, time
from pprint import pprint
from functools import reduce

# random.seed(42)

# for a given feedback, calculate all rule keys, and randomly generate rule values

FEEDBACK = 3
# with FEEDBACK = 4 there are 2**4 possibilities. which is only 16.
# with 3 it's 8
# so there are some cool sequences here, but nothing like the CA generation in 2D.
# it needs to generate more than one additional step

def get_rules(feedback):
    keys = [tuple([int(s) for s in list(format(n, 'b').zfill(feedback))]) for n in range(2**feedback)]
    values = [random.choice((1, 0)) for n in range(2**feedback)]
    rules = dict(zip(keys, values))
    pprint(rules)
    return rules, keys

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a    

def find_period(sequence):
    factors = []
    for length in range(2, (len(sequence) // 2) + 1):
        chunk_1, chunk_2 = sequence[-length:], sequence[-length * 2:(-length * 2) + length]
        if chunk_1 == chunk_2:
            factors.append(length)
    return reduce(gcd, factors)            


rules, seeds = get_rules(FEEDBACK)

best_seed = None
best_sequence = None
longest_period = 0
for seed in seeds:
    sequence = []
    sequence += seed
    for x in range(FEEDBACK * 10):
        sequence.append(rules[tuple(sequence[-FEEDBACK:])])
    period = find_period(sequence)
    if period > longest_period:
        longest_period = period
        best_seed = seed
        best_sequence = sequence
print(best_seed)
print(longest_period)
print(best_sequence[-longest_period:])


# ok, then test for oscillations or repeatability or something. entropy?    
# basically the longest oscillation time
# hmm. does it always have a repeating result?