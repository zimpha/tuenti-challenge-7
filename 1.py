for i in xrange(int(raw_input())):
    n = int(raw_input())
    s = sum(map(int, raw_input().split(' ')))
    print 'Case #%d: %d' % (i + 1, (s + 7) / 8)
