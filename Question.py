#WAP to calculate the binary representation for number 39:100111 2.
n=39
remainders=[]
while n>0: #dont know how much time it take
    remainder=n%2    #remainder of division by 2
    remainders.append(remainder)   #we keep track of remainders
    n//=2   #we divide n by 2 using Floor division-int part only
    #reassign the list to its reversed copy and print it
    remainders=remainders[::-1]    #print the items from last to beginning
    print(remainders)
    