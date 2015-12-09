#! /usr/bin/env python

# Day 1: Not Quite Lisp
# http://adventofcode.com/day/1
with open('input/Day01.txt') as f:
    data = f.read()


# Part 1
print 'You end up on floor {}'.format(
    reduce(lambda x, i: x + 1 if i == '(' else x - 1, data, 0))


# Part 2
floor = 0
for iteration, instruction in enumerate(data, start=1):
    floor = floor + 1 if instruction == '(' else floor - 1
    if floor < 0:
        print 'You hit the basement on iteration {}'.format(iteration)
        break
