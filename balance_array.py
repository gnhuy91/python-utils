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
    # Slow performance, need optimization

    # Iterate from 1->N-1 instead of 0->N or 1->N+1, b/c the `balance` index
    # can not be 0 or N, checking for them is pointless.
    # Also iterate from 1->N-1 is obviously faster than 0->N or 1->N+1.
    for i in range(1, len(A)):
        left_sum = sum(A[:i-1])
        right_sum = sum(A[i:])

        if left_sum == right_sum:
            return i

    return None

def balanceSum2(A):
    # currently is wrong
    left_sum, right_sum = 0, sum(A)

    for i, value in enumerate(A):
        i += 1

        if left_sum == right_sum:
            return i

        left_sum += A[i-1]
        right_sum -= A[i]

        print i, left_sum, right_sum

    return None

def test_one(func):
    inp = [4,1,2,3,3]
    out = 3

    if out != func(inp):
        return False
    return True

def test_two(func):
    inp = [3,1,2,1]
    out = 2

    if out != func(inp):
        return False
    return True

def test_three(func):
    inp = [3,1,3,1]
    out = 2

    if out != func(inp):
        return False
    return True

def main():
    test_func = balanceSum
    print test_one(test_func)
    print test_two(test_func)
    print test_three(test_func)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
