def test(n):
    if n>1:
        print(n)
        test(n/2)


#t(n) = 1 cuando n=1
#t(n) = t(n/2) +1 cuando n>1