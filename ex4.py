def gen(n):
    i = 0 
    while i<=n:
        yield i
        i = i+1
g = gen(5)
l1 =list(g)
print(l1)
