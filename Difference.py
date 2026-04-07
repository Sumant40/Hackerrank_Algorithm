#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n=len(arr)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += arr[i][i]           # Left-to-right diagonal
        secondary_sum += arr[i][n-i-1]    # Right-to-left diagonal
    
    return abs(primary_sum - secondary_sum)
