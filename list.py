def chunks(l, n):
    '''
    :rtype list
    split a list into a list of sublists
    '''
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
