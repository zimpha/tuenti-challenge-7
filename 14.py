import telnetlib

tn = telnetlib.Telnet('52.49.91.111', 2121)

print tn.read_until('...')
print tn.read_until('Good luck!')

coin = 200
turn = 1
while True:
    tn.read_until('CHOOSE\n')
    tn.write('+bet10\n')
    tn.read_until('DEALER CARDS ')
    print tn.read_until('\n')
    while True:
        tn.read_until('CURRENT VALUES '),
        value = eval(tn.read_until(']'))
        if min(value) > 21:
            break
        print tn.read_until('CHOOSE\n')
        print value
        tn.write('+stand\n')
        break
    '''
        if len(value) == 1:
            print 'auto: ',
            if value[0] <= 17:
                tn.write('+stand\n')
                print 's'
                break
            else:
                tn.write('+hit\n')
                print 'h'
        else:
            print 'input: ',
            x = raw_input()
            if x == 'h':
                tn.write('+hit\n')
            else:
                tn.write('+stand\n')
                break
    '''
    tn.read_until('RESULT ')
    tn.read_until(': '),
    data = tn.read_until('\n')
    print 'Turn #%d:' % turn, data
    if data[:3] == 'TIE':
        coin += 0
    elif data[:3] == 'WIN':
        coin += 10
    else:
        coin -= 10
    turn += 1
    if coin < 0:
        print tn.read_all()
        break
