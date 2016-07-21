'''
`Balance Array`

Find i in array A where: A[1] + A[2]...A[i-1] = A[i+1] + A[i+2]...A[len(A)]

Write a `balanceSum` function which take an integer array as input,
it should return the smallest i, where i is an index in the array such that
the sum of elements to its left is equal to the sum of elements to its right.

Note: There always exist a solution.
'''

'''
TODO: use `pytest` or the likes to run tests more easily.
'''


def balanceSum(A):
    # O(N^2)

    # Iterate from 1->N-1 instead of 0->N or 1->N+1, b/c the `balance` index
    # can not be 0 or N, checking for them is pointless.
    # Also iterate from 1->N-1 is obviously faster than 0->N or 1->N+1.

    # print A
    for i in range(1, len(A) - 1):
        left_sum = sum(A[:i])
        right_sum = sum(A[i + 1:])

        # print i, " ", left_sum, right_sum

        if left_sum == right_sum:
            return i + 1  # index starts from 1

    return None


def balanceSum2(A):
    # O(2N)
    # reduced number of sum()

    # start from A[1]
    left_sum, right_sum = A[0], sum(A[2:])
    if left_sum == right_sum:
        return 1 + 1  # index starts from 1

    # print A, left_sum, right_sum

    for i in range(2, len(A) - 1):
        left_sum += A[i - 1]
        right_sum -= A[i]

        # print i + 1, " ", left_sum, right_sum

        if left_sum == right_sum:
            return i + 1

    return None


def test_one(func):
    inp = [4, 1, 2, 3, 3]
    out = 3

    fout = func(inp)
    if out != fout:
        print ("want %s, got %s" % (out, fout))
        return False
    return True


def test_two(func):
    inp = [3, 1, 2, 1]
    out = 2

    fout = func(inp)
    if out != fout:
        print ("want %s, got %s" % (out, fout))
        return False
    return True


def test_three(func):
    inp = [3, 1, 3, 1]
    out = 2

    fout = func(inp)
    if out != fout:
        print ("want %s, got %s" % (out, fout))
        return False
    return True


def test_four(func):
    inp = [3, 1, 2, 4]
    out = 3

    fout = func(inp)
    if out != fout:
        print ("want %s, got %s" % (out, fout))
        return False
    return True


def main():
    test_func = balanceSum2
    print test_one(test_func), "\n"
    print test_two(test_func), "\n"
    print test_three(test_func), "\n"
    print test_four(test_func), "\n"

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
