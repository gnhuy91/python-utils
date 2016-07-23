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


if __name__ == '__main__':
    arr = [12, 4, 5, 6, 7, 3, 1, 15]
    quick_sort(arr, 0, len(arr) - 1)
    print arr
