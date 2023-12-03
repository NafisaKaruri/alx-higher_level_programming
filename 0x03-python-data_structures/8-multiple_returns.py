#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        return len((None, )), None
    tup = tuple(sentence)
    return len(tup), tup[0]
