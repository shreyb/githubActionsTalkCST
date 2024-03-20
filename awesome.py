#!/usr/bin/env python3

def add_two_ints(a: int, b: int) -> int:
    if (not isinstance(a, int)) or (not isinstance(b,int)):
        raise TypeError("One of the input values is NOT an int!!")
    return a + b

def subtract_two_ints(a: int, b: int) -> int:
    if (not isinstance(a, int)) or (not isinstance(b,int)):
        raise TypeError("One of the input values is NOT an int!!")
    return a - b
