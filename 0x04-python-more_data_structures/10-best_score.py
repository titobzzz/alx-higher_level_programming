#!/usr/bin/python3
def best_score(a_dictionary):
    '''  Return:
        key of with biggest int value
    '''
    if not isinstance(a_dictionary, dict):
        return None

    max_a = list(a_dictionary.values())[0]
    max_b = list(a_dictionary)[0]

    for b, a in a_dictionary.items():
        if a > max_a:
            max_a = a
            max_b = b

    return max_b
