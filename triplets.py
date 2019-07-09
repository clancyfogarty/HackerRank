#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    tripA = 0
    tripB = 0
    for i in range(3):
        if a[i] > b[i]:
            tripA = tripA + 1
        if a[i] < b[i]:
            tripB = tripB + 1
    return(tripA,tripB)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
