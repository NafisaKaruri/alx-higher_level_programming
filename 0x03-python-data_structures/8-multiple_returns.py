#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return 0, None
    tup = tuple(sentence)
    return len(tup), tup[0]
