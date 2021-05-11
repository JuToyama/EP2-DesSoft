def possui_movimentos_possiveis(l):
    i=0
    a=1
    b=l[i]
    c=l[i+1]
    d=0
    ii=0
    print(len(l))
    while i<len(l)-1:
        b=l[i]
        c=l[i+1]
        if b[0]==c[1]:
            return True
        i+=1
    while ii<len(l)-3:
        b=l[ii]
        d=l[ii+3]
        if b[1]==d[1]:
            return True
        ii+=1
    if ii>=len(l)-3:
        return False