#!/bin/python

import sys
import os

# Count the number of friend groups by counting the number of connected components.
# This is done by iterating through every node and doing a BFS if the node
# has not already been visited in a prior BFS. Every time a new BFS is started,
# the node is the first in a new connected component, so increment the count by 1.

from collections import deque

def friendCircles(friends):

    circle_count = 0
    visited = set()

    for friend in range(len(friends)):
        if friend not in visited:
            circle_count += 1
            agenda = deque([friend])
            while len(agenda) > 0:
                i = agenda.popleft()
                visited.add(i)
                for j in range(len(friends)):
                    if friends[i][j] is 'Y' and j not in visited:
                        agenda.append(j)

    return circle_count

_friends_cnt = int(input())
_friends_i=0
_friends = []
while _friends_i < _friends_cnt:
    _friends_item = input()
    _friends.append(_friends_item)
    _friends_i+=1

res = friendCircles(_friends);
print(res)
