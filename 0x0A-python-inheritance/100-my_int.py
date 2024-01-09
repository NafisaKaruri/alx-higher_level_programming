#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """MyInt class child of int that repel == and !="""
    def __eq__(self, other):
        """Inverts equal to not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts not equal to equal"""
        return super().__eq__(other)
