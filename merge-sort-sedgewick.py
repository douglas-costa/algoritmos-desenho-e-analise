from math import floor
from sys import maxsize

def merge_sort(arr, left, right):
    aux = arr[:]

    def _merge_sort(arr, left, right):
        if left < right:
            middle = floor((left + right) / 2)

            _merge_sort(arr, left, middle)
            _merge_sort(arr, middle + 1, right)

            merge(arr, left, middle, right)

    def merge(arr, left, middle, right):
        _right = right + 1

        aux[left:_right] = arr[left:_right]

        i = left
        j = middle + 1

        for k in range(left, _right):
            if i > middle:
                arr[k] = aux[j]
                j += 1
            elif j > right:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1

    _merge_sort(arr, left, right)