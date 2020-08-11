

def dig(n):
    res = 0
    i = 0
    j = 1
    while i < n:
        res += j*9
        j *= 10
        i += 1
    return res

def pages(n):
    i = 0
    j = 1
    
    while True:
        if n > dig(j-1):
            if n < dig(j):
                i += (n - dig(j-1) )/ j
                print(i)
            else:
                i += dig(j) / j
                print(i)
        else:
            return i
        j += 1
        
            
i = int(input())
print(pages(i))


