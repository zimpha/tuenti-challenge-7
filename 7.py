from websocket import create_connection
import base64

ws = create_connection("ws://52.49.91.111:3636/word-soup-challenge")

def append(s):
    s = s + '-saltbae'
    r = 0
    for e in s:
        r = (r << 5) - r + ord(e)
    r %= 2 ** 32
    if r >= 2 ** 31:
        r = 2 ** 32 - r
    return r

def get_board():
    result = base64.b64decode(ws.recv())
    i = 0
    n, m = 0, 0
    s = []
    w = []
    while i < len(result):
        if result[i:i+2] == 'n=':
            i += 2
            while result[i] >= '0' and result[i] <= '9':
                n = n * 10 + ord(result[i]) - ord('0')
                i += 1
        if result[i:i+2] == 'e=':
            i += 2
            while result[i] >= '0' and result[i] <= '9':
                m = m * 10 + ord(result[i]) - ord('0')
                i += 1
        if result[i:i+2] == 's=':
            i += 4
            j = i
            while result[j] != ']' or result[j + 1] != ']':
                j += 1
            s = result[i : j].split('],[')
            s = [[x[1:-1] for x in e.split(',')] for e in s]
            i = j
        if result[i:i+2] == 'c=':
            i += 3
            j = i
            while result[j] != ']':
                j += 1
            w = result[i: j].split(',')
            w = [x[1:-1] for x in w]
            break
        i += 1
    return n, m, s, w

def search(s):
    l = len(s)
    for t in xrange(m):
        for e in xrange(n):
            if t - l + 1 >= 0: # up
                flag = True
                for i in xrange(l):
                    if g[t - i][e] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e, t - l + 1)
            if t + l - 1 < m: # down
                flag = True
                for i in xrange(l):
                    if g[t + i][e] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e, t + l - 1)
            if e - l + 1 >= 0: # left
                flag = True
                for i in xrange(l):
                    if g[t][e - i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e - l + 1, t)
            if e + l - 1 < n: # right
                flag = True
                for i in xrange(l):
                    if g[t][e + i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e + l - 1, t)
            if t - l + 1 >= 0 and e - l + 1 >= 0: # up-left
                flag = True
                for i in xrange(l):
                    if g[t - i][e - i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e - l + 1, t - l + 1)
            if t - l + 1 >= 0 and e + l - 1 < n: # up-right
                flag = True
                for i in xrange(l):
                    if g[t - i][e + i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e + l - 1, t - l + 1)
            if t + l - 1 < m and e - l + 1 >= 0: # down-left
                flag = True
                for i in xrange(l):
                    if g[t + i][e - i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e - l + 1, t + l - 1)
            if t + l - 1 < m and e + l - 1 < n: # up-left
                flag = True
                for i in xrange(l):
                    if g[t + i][e + i] != s[i]:
                        flag = False
                if flag:
                    return '%d-%d-%d-%d' % (e, t, e + l - 1, t + l - 1)
    return None

n, m, g, w = get_board()
for e in w:
    s = search(e)
    ws.send(base64.b64encode(s + '-' + str(append(s))))
    ws.recv()
print base64.b64decode(ws.recv())

ws.send('play hard')

n, m, g, w = get_board()
for e in w:
    s = search(e)
    ws.send(base64.b64encode(s + '-' + str(append(s))))
    print base64.b64decode(ws.recv())
print base64.b64decode(ws.recv())
