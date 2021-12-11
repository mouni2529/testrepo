def fib():
    i,j=0,1
    while True:
        yield i
        i,j =j,i+j
for f in fib():
    if f>100:
        break
    print(f)
