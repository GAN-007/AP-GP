
"""ARITHMETIC PROGRESSION"""
"""\\\\\\\\\\\/////////////////\\\\\\\\\\\\//////////////////////\\\\\\\\\\\\\\\\\\\//////////"""
'''We know the Arithmetic Progression series is like = 2, 5, 8, 11, 14 …. … 
In this series 2 is the stating term of the series . 
Common difference = 5 – 2 = 3 (Difference common in the series). 
so we can write the series as : 
t1 = a1 
t2 = a1 + (2-1) * d 
t3 = a1 + (3-1) * d 
. 
. 
. 
tn = a1 + (n-1) * d 
 

 '''
a=int(input("Whats your first number"))
d=int(input("whts your common difference"))
n=int(input( "Whats your Nth term?"))
print("This is the Arithmetic Series")
g=1
while(g<=n):
    tg = a + (g-1)*d
    print(tg)
    g=g+1

print("Subscribe to Geox Rhymes") 
