#! /usr/bin/env python

import hashlib

# Day 4: The Ideal Stocking Stuffer
# http://adventofcode.com/day/4
data = 'ckczppom'


# Shared
def hash_gen(d):
    i = 0
    while True:
        yield (i, hashlib.md5('{}{}'.format(d, i)).hexdigest())
        i += 1

# Part 1
for i, h in hash_gen(data):
    if h.startswith('0' * 5):
        print ('The first number to create a five zero prefixed hash when '
               'appended to "{}" is "{}"').format(data, i)
        break


# Part 2
for i, h in hash_gen(data):
    if h.startswith('0' * 6):
        print ('The first number to create a six zero prefixed hash when '
               'appended to "{}" is "{}"').format(data, i)
        break
