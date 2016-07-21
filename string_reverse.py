inp = 'hello, world'
out = inp[::-1]


def string_reverse(s):
    # O(n)

    r = []
    for i in range(len(s) - 1, -1, -1):
        r.append(s[i])

    return ''.join(r)


def main():
    fout = string_reverse(inp)
    print inp, '->', fout

    if fout != out:
        print "want '%s', got '%s'" % (out, fout)
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))
