def calc(S, D):
    ret = D / 2 * 2
    D %= 2
    if S >= D * 2:
        return ret + S / 2 * 2 + D
    else:
        return ret

for cas in xrange(int(raw_input())):
    print 'Case #%d:' % (cas + 1),
    S, C, D = map(int, raw_input().split(' '))
    C = C / 2 * 2
    ret = 0
    if C >= 4:
        ret = max(ret, 4 + calc(S, D))
    if C >= 6:
        if S >= 2:
            ret = max(ret, 8 + calc(S - 2, D))
        if D >= 1 and S >= 2:
            ret = max(ret, 9 + calc(S - 2, D - 1))
    if C >= 8:
        if D >= 1:
            ret = max(ret, 9 + calc(S, D - 1))
        if S >= 2:
            ret = max(ret, 10 + calc(S - 2, D))
        if D >= 2:
            ret = max(ret, 10 + calc(S, D - 2))
    if C >= 10:
        if D >= 1 and S >= 4:
            ret = max(ret, 15 + calc(S - 4, D - 1))
        if D >= 2 and S >= 2:
            ret = max(ret, 14 + calc(S - 2, D - 2))
        if S >= 2:
            ret = max(ret, 12 + calc(S - 2, D))
        if D >= 1 and S >= 2:
            ret = max(ret, 13 + calc(S - 2, D - 1))
        if S >= 4:
            ret = max(ret, 14 + calc(S - 4, D))
    if C >= 12:
        now = C / 4 * 4
        ret = max(ret, now + calc(S, D))
        if D % 2 == 1:
            ret = max(ret, now + 1 + calc(S, D - 1))
        if S >= 2:
            ret = max(ret, now + 2 + calc(S - 2, D))
        if C - now >= 2 and S >= 2:
            ret = max(ret, now + 4 + calc(S - 2, D))
            if D >= 1:
                ret = max(ret, now + 5 + calc(S - 2, D - 1))
    print ret
