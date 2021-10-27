def test(n):
    if n>0:
        for i in n:
            print(n)
        test(n-1)


#        / 1            n=0
#t(n) -- | t(n-1) + n   n>0
#        /


# t(n) = t(n - k) + (n - (k-1)) + (n - (k-2)) + (n - (k-3)) ...  + (n - 1) + n

