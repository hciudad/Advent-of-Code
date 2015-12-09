#! /usr/bin/env python

from itertools import izip_longest

# Day 3: Perfectly Spherical Houses in a Vacuum
# http://adventofcode.com/day/3
with open('input/Day03.txt') as f:
    data = f.read()


# Shared
class GPS:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

        self._visited = set()
        self._visited.add((self._x, self._y))

    def update_location(self, direction):
        if direction == '>':
            self._x += 1
        elif direction == 'v':
            self._y += 1
        elif direction == '<':
            self._x -= 1
        elif direction == '^':
            self._y -= 1
        else:
            raise Exception('invalid direction: {}'.format(direction))

        self._visited.add((self._x, self._y))

        return self

    def total_visits(self):
        return len(self._visited)

    def visited(self):
        return self._visited

# Part 1
print 'Total houses visited by Santa: {}'.format(
    reduce(lambda g, d: g.update_location(d), data, GPS()).total_visits())


# Part 2
santa = GPS()
robo_santa = GPS()
for s, r in izip_longest(*([iter(data)] * 2), fillvalue='x'):
    santa.update_location(s)
    robo_santa.update_location(r)

total_visited = santa.visited()
total_visited.update(robo_santa.visited())
print 'Total houses visited by Santa and Robo-Santa: {}'.format(
    len(total_visited))
