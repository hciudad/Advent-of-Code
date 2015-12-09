#! /usr/bin/env python

import re

# Day 5: Doesn't He Have Intern-Elves For This?
# http://adventofcode.com/day/5
with open('input/Day05.txt') as f:
    data = f.readlines()

# Part 1
bad_duos = re.compile('(ab|cd|pq|xy)', re.I)


def vowel_count(string):
    return len(filter(lambda x: x in 'a e i o u'.split(), string))


def has_dupe_chars(string):
    for i, s in enumerate(string, start=1):
        if i == len(string):
            return False
        if s == string[i]:
            return True
    return False


def is_good_v1(string):
    if vowel_count(string) < 3:
        return False
    if not has_dupe_chars(string):
        return False
    if bad_duos.search(string):
        return False
    return True

print 'Good strings (v1): {}'.format(len(filter(is_good_v1, data)))


# Part 2
def has_non_overlapping_pairs(string):
    for i in range(len(string) - 1):
        pair = string[i: i + 2]
        if pair in string[i + 2:]:
            return True
    return False


def has_split_dupe_chars(string):
    for i, s in enumerate(string, start=1):
        if i + 1 == len(string):
            return False
        if s == string[i + 1]:
            return True
    return False


def is_good_v2(string):
    if not has_non_overlapping_pairs(string):
        return False
    if not has_split_dupe_chars(string):
        return False
    return True

print 'Good strings (v2): {}'.format(len(filter(is_good_v2, data)))
