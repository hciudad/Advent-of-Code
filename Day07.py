#! /usr/bin/env python

from collections import deque
import re

# Day 7: Some Assembly Required
# http://adventofcode.com/day/7
with open('input/Day07.txt') as f:
    data = f.readlines()


# Shared
class Circuit:
    instruction_re = re.compile(r'^(?P<src_wire1>[a-z]+)?(?P<src_value>\d+)?'
                                r'\s?(?P<gate>(AND|OR|LSHIFT|RSHIFT|NOT))?'
                                r'\s?(?P<src_wire2>[a-z]+)?'
                                r'(?P<signal_or_shiftdist>\d+)?'
                                r' -> (?P<dest_wire>[a-z]+)')

    def __init__(self, **signal_overrides):
        self._wires = signal_overrides
        self._instructions = deque()

    def get_value(self, gate=None, src_wire1=None, src_wire2=None,
                  src_value=None, signal_or_shiftdist=None, dest_wire=None):
        if gate is None:
            value = int(src_value or self._wires[src_wire1])
        elif gate == 'AND':
            value = int(
                src_value or self._wires[src_wire1]) & self._wires[src_wire2]
        elif gate == 'OR':
            value = self._wires[src_wire1] | self._wires[src_wire2]
        elif gate == 'LSHIFT':
            value = self._wires[src_wire1] << int(signal_or_shiftdist)
        elif gate == 'RSHIFT':
            value = self._wires[src_wire1] >> int(signal_or_shiftdist)
        elif gate == 'NOT':
            value = 65536 + ~self._wires[src_wire2]
        else:
            raise Exception('Invalid gate: {}'.format(gate))

        return int(value)

    def wire(self, name):
        return self._wires[name]

    def list_wires(self):
        wire_names = self._wires.keys()
        wire_names.sort()
        print 'The signal provided to each wire:\n{}'.format(
            '\n'.join('{}: {}'.format(wire_name, self._wires[wire_name])
                      for wire_name in wire_names))

    def process(self, instructions):
        self._instructions.extend(instructions)

        iterations = 0
        while self._instructions:
            iterations += 1
            instruction = self._instructions.popleft()
            parts = self.instruction_re.match(instruction).groupdict()

            if parts['dest_wire'] in self._wires:
                continue

            try:
                self._wires[parts['dest_wire']] = self.get_value(**parts)
            except KeyError:
                self._instructions.append(instruction)

        return iterations


# Part 1
c1 = Circuit()
iterations = c1.process(data)
print 'The value for wire `a` is {}'.format(c1.wire('a'))
print 'Num of iterations: {}'.format(iterations)

# Part 2
c2 = Circuit(b=c1.wire('a'),)
iterations = c2.process(data)
print 'The value for wire `a` is now {}'.format(c2.wire('a'))
print 'Num of iterations: {}'.format(iterations)
