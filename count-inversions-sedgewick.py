from math import floor
from sys import maxsize

def count_inversions(arr):
    aux = arr[:]

    def _count_inversions(arr, left, right):
        if left >= right:
            return 0

        middle = floor((left + right) / 2)

        x = _count_inversions(arr, left, middle)
        y = _count_inversions(arr, middle + 1, right)

        z = _count_split_inversions(arr, left, middle, right)

        return x + y + z

    def _count_split_inversions(arr, left, middle, right):
        _middle = middle + 1
        _right  = right + 1

        aux[left:_right] = arr[left:_right]

        i     = left
        j     = middle + 1
        total = 0

        for k in range(left, _right):
            if i > middle:
                arr[k] = aux[j]
                j      += 1
                total  += _middle - i
            elif j > right:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j      += 1
                total  += _middle - i
            else:
                arr[k] = aux[i]
                i += 1

        return total

    return _count_inversions(arr, 0, len(arr) - 1)