'''
QuickSort implementation
'''


def quick_sort(arr, l, r):
    i, j = l, r
    x = arr[(l + r) / 2]

    if len(arr) == 0:
        return arr

    while True:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        if i >= j:
            break

        if l < j:
            quick_sort(arr, l, j)
        if i < r:
            quick_sort(arr, i, r)


def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    if begin >= end:
        return

    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot - 1)
    quicksort(array, pivot + 1, end)


if __name__ == '__main__':
    arr = [12, 2, 8, 5, 1, 6, 4, 15]
    quicksort(arr, 0, len(arr) - 1)
    print arr
