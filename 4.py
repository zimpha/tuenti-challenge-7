for cas in xrange(int(raw_input())):
    print 'Case #%d:' % (cas + 1),
    a = map(int, raw_input().split(' '))[1:]
    a.sort()
    ret = -1
    for i in xrange(2, len(a)):
        b = a[i - 1]
        c = a[i]
        if a[i - 2] <= c - b:
            continue
        l, r = 0, i - 2
        while l < r:
            m = (l + r) / 2
            if a[m] > c - b:
                r = m
            else:
                l = m + 1
        if ret == -1 or ret > b + c + a[l]:
            ret = b + c + a[l]
    if ret == -1:
        ret = 'IMPOSSIBLE'
    print ret
