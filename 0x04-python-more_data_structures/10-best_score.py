#!/usr/bin/python3
def best_score(a_dictionary):
    '''Findsa key with biggest integer value in a dictionary
    Return:
        key with biggest int value
    '''
    if not isinstance(a_dictionary, dict):
        return None

    max_v = list(a_dictionary.values())[0]
    max_k = list(a_dictionary)[0]

    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            max_k = k

    return max_k
