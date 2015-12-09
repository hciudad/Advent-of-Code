#! /usr/bin/env python

import re

# Day 8: Matchsticks
# http://adventofcode.com/day/8
with open('input/Day08.txt') as f:
    data = f.readlines()


# Part 1
literal_chars, in_memory_chars = reduce(lambda x, y: (
    x[0] + len(y.strip()),
    x[1] + len(eval(y.strip()))),
    data, (0, 0))
print 'literal characters: {}'.format(literal_chars)
print 'in memory characters: {}'.format(in_memory_chars)
print 'part one difference: {}\n'.format(literal_chars - in_memory_chars)

# Part 2
literal_chars, escaped_chars = reduce(lambda x, y: (
    x[0] + len(y.strip()),
    x[1] + len(re.escape(y.strip())) + 2),  # to cover wrapping quotes
    data, (0, 0))
print 'literal characters: {}'.format(literal_chars)
print 'escaped characters: {}'.format(escaped_chars)
print 'part two difference: {}\n'.format(escaped_chars - literal_chars)
