#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''Adds all unique integers in a list
    '''
    uniq_sum = 0
    for n in set(my_list):
        uniq_sum += n
    return uniq_sum
