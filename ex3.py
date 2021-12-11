def countdown(num):
    print("starts countdown")
    while num>0:
        yield num
        num = num-1
g = countdown(10)
for i in g:
    print(i)
