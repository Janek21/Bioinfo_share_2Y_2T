def canvi(c, n, s):
    # Initialize the dp array with infinity for all amounts except 0
    dp = [float('inf')] * (c + 1)
    dp[0] = 0 #assign 0 as the base
    for i in range(n):  #loop through the coins
        for j in range(s[i], c + 1): #loop through all amounts of the value of current coin up until the goal 
            dp[j] = min(dp[j], 1 + dp[j - s[i]])    #find the minimum amount between keeping it the current way or substracting the value of our coin from the quantity +1 considering the current coin

    if dp[c] > c:   #if the value at the goal is bigger than the goal then its infinity so we did not find an optimal solution
        return "no"
    else:   #if the value is smaller than the goal 
        return dp[c] #return the minimal value to obtain the goal
        
        
def read():
    c=int(itm())
    n=int(itm())
    s=[]
    for i in range(n):
        s.append(int(itm()))
    return c, n, s


from pytokr import pytokr
itm=pytokr()
while itm:
    c, n, s=read()
    res= canvi(c, n, s)
    print (res) 
