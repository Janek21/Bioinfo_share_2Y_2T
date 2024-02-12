from pytokr import pytokr
def canvi_minim(c, n, s):
    dp = [float('inf')] * (c + 1)
    dp[0] = 0 
    for i in range(n): 
        for j in range(s[i], c + 1):  
            dp[j] = min(dp[j], 1 + dp[j - s[i]])    
    if dp[c] > c:   
        return "no"
    else:    
        return dp[c]
        
        
item = pytokr()
while True:
    s = list()
    c = int(item())
    n = int(item())
    for x in range(n):
        s.append(int(item()))
    sol = canvi_minim(c,n,s)
    print(sol)

