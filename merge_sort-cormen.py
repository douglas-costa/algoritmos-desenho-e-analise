from math import floor
from sys import maxsize

def merge_sort(arr, left, right):
    if left < right:
        middle = floor((left + right) / 2)

        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)

        merge(arr, left, middle, right)

def merge(arr, left, middle, right):
    _middle = middle + 1
    _right  = right + 1

    L = arr[left:_middle] + [maxsize]
    R = arr[_middle:_right] + [maxsize]

    i, j = 0, 0

    for k in range(left, _right):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            arr[k] = R[j]
            j += 1