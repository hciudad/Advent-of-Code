#! /usr/bin/env python

# Day 2: I Was Told There Would Be No Math
# http://adventofcode.com/day/2
with open('input/Day02.txt') as f:
    data = f.readlines()


# Part 1
def area_calc_plus(l, w, h):
    [s1, s2, s3] = (l * w, w * h, l * h)
    return (s1 * 2) + (s2 * 2) + (s3 * 2) + min(s1, s2, s3)

print reduce(lambda y, d: y + area_calc_plus(
    *map(int, d.split('x'))), data, 0)


# Part 2
def ribbon_calc(l, w, h):
    [p1, p2, p3] = ((l + w) * 2, (w + h) * 2, (l + h) * 2)
    return min(p1, p2, p3) + (l * w * h)

print reduce(lambda y, d: y + ribbon_calc(
    *map(int, d.split('x'))), data, 0)
