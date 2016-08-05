#! /usr/bin/python
# utf-8

lst=['bc', 'abc', 1, 'abc', 'guo', 1, 2, 3, [1, 2, 3]]


pos = int(0)
for i in range(lst.count(1)):
    first_pos = lst[pos:].index(1)
    print "find index of i: ", pos + first_pos
    pos = first_pos +int(1)
    #print "pos: ",first_pos

