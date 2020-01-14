def hanoi(n,A,B,C,l={}):
    if n>0:
        hanoi(n-1,A,C,B,l)
        print('%s->%s'%(A,C))
        l['count'] = l.get('count',0) + 1
        # global i
        # i += 1
        hanoi(n-1,B,A,C,l)
    return l.get('count',0)

print(hanoi(0, 'A', 'B', 'C'))
