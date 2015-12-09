#! /usr/bin/env python

import re

# Day 6: Probably a Fire Hazard
# http://adventofcode.com/day/6
with open('input/Day06.txt') as f:
    data = f.readlines()

# Shared
action_re = re.compile((r'^(?P<action>.+) (?P<start_x>\d+),(?P<start_y>\d+) '
                       r'through (?P<end_x>\d+),(?P<end_y>\d+)$'))


class Grid:
    def __init__(self, width=1000, height=1000, init_state='off'):
        self._bulbs = {(x, y): dict(
                       state=(init_state is 'on'),
                       brightness=0)
                       for x in range(width)
                       for y in range(height)}

    def range_action(self, action=None, start_x=None,
                     start_y=None, end_x=None, end_y=None):
        action = action.replace(' ', '_')
        for x in range(int(start_x), int(end_x) + 1):
            for y in range(int(start_y), int(end_y) + 1):
                getattr(self, action)(x, y)

    def turn_on(self, x, y):
        self._bulbs[(x, y)]['state'] = True
        self._bulbs[(x, y)]['brightness'] += 1

    def turn_off(self, x, y):
        self._bulbs[(x, y)]['state'] = False
        self._bulbs[(x, y)]['brightness'] -= 1
        if self._bulbs[(x, y)]['brightness'] < 0:
            self._bulbs[(x, y)]['brightness'] = 0

    def toggle(self, x, y):
        self._bulbs[(x, y)]['state'] = not self._bulbs[(x, y)]['state']
        self._bulbs[(x, y)]['brightness'] += 2

    def count_on(self):
        return len(filter(lambda x: x['state'] is True, self._bulbs.values()))

    def total_brightness(self):
        return reduce(lambda x, y: x + y['brightness'],
                      self._bulbs.values(), 0)


grid = Grid()
for action_str in data:
    grid.range_action(**action_re.match(action_str).groupdict())

# Part 1
print '{} lights are lit'.format(grid.count_on())


# Part 2
print 'Total brightness: {}'.format(grid.total_brightness())
