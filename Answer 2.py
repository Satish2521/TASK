p = [6, 2, 3, 2, 1] 
n = len(p)
def x(p, start, end): 
    print ("[ ", end = "") 
    for i in range(start, end+1): 
        print (p[i], end =" ") 
    print ("]", end ="") 

def split(p, n):
    leftsum = 0
    for i in range(0, n): 
        leftsum += p[i]
    rightsum = 0
    for i in range(0, n):
        if 2 * rightsum + p[i] == leftsum:
            x(p, 0, i - 1)
            x(p, i + 1, n - 1)
            return True
        rightsum += p[i]
    return False

print (split(p, n), end = "")
