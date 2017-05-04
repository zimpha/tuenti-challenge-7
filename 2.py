for cas in xrange(int(raw_input())):
    print 'Case #%d:' % (cas + 1),
    n = int(raw_input())
    a = map(int, raw_input().split(' '))
    s = 0
    i = 0
    frame = 0
    bonus = 0
    strike = False
    spare = False
    while frame < 10:
        s += a[i]
        frame += 1
        if a[i] == 10:
            s += a[i + 1] + a[i + 2]
            i += 1
        elif a[i] + a[i + 1] == 10:
            s += a[i + 1] + a[i + 2]
            i += 2
        else:
            s += a[i + 1]
            i += 2
        if frame == 10:
            print s
        else:
            print s,
    assert frame == 10
