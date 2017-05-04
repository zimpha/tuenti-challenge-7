for cas in xrange(int(raw_input())):
    print 'Case #%d:' % (cas + 1),
    P = int(raw_input())
    now = 0
    ret = 0
    while now < P:
        now += now + 1
        ret += 1
    print ret
