def test(n):
    i=1
    if n>0:
        for i in range(n):
            print(i)
            i=i*2
        print("\n")
        test(n-1)
        

test(3)



#t(n)   {1;    n=0
#       {t(n-1) + lon(n)  n>0


#t(n) = t(n-k) + log(1) + log(2) + log(3) ... + log(n - 1) + log(n)

#t(n) = t(0) + log n!
#t(n) = 1 + log(n!)

# O(nlog(n))