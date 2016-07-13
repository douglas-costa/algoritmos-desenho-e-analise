from math import floor
from sys import maxsize

def count_inversions(arr, left, right):
    if left >= right:
        return 0

    middle = floor((left + right) / 2)

    x = count_inversions(arr, left, middle)
    y = count_inversions(arr, middle + 1, right)

    z = merge_count_inversions(arr, left, middle, right)

    return x + y + z

def merge_count_inversions(arr, left, middle, right):
    _middle = middle + 1
    _right  = right + 1

    L = arr[left:_middle] + [maxsize]
    R = arr[_middle:_right] + [maxsize]

    i     = 0
    j     = 0
    total = 0

    for k in range(left, _right):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            arr[k] = R[j]
            j += 1

            total += _middle - left - i

    return total