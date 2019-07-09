#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    length = len(arr)
    for x in arr:
        if x < 0:
            neg = neg + 1
        if 0 < x:
            pos = pos + 1
        if x == 0:
            zero = zero + 1
    print('{:.6f}'.format(pos/length))
    print('{:.6f}'.format(neg/length))
    print('{:.6f}'.format(zero/length))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
