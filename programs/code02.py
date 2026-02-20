def fiboLoop():
    p2 = 0
    p1 = 1
    for f in range(10):
        newF = p1 + p2
        print(newF)
        p2 = p1
        p1 = newF

def fiboRecur(p1, p2):
    global count
    if count <= 19:
        newF = p1 + p2
        print(newF)
        p2 = p1
        p1 = newF
        count += 1
        fiboRecur(p1, p2)
    else:
        return
    
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)