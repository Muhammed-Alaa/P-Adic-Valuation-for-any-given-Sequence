lst=[]


lop = 100
for i in range(lop+1):
    lst.append(-1)

"The previous part is just to avoid the overflow of calculation for the same values everytime and the change of lop value, will give you more or less from the sequence no."
    
def padovan(i):
    if lst[i] != -1:
        return lst[i];
    if i == 0 or i == 1 or i == 2:
        return 1
    else:
        lst[i] = ((padovan(i-2))+padovan(i-3))
        return lst[i]
    
"The previous part is to define the sequence, we can change it's name, here I use sequence called Padovan, you can use any other sequence like Fibonacci"
"You will just have to change the name, change the beginning values and to change the function or recursive formula"

for i in range(lop+1):
    padovan(i)
    
"The previous part is to save the sequence entries"    
    
"The p-adic valuation is to see the number contain how much of this prime, for example, 9 contains 3 twice (3 power 2), so the 3 adic valuation for 9 is 2"
"But What about 18? The 3 adic valuation for 18 is also 2, because it is 9 times 2, and the 3 adic valuation for 9 is 2 and the 3 adic valuation for 2 is zero, so 2+0 = 2"
"You can change the p adic base from changing the value of the following: paddic, but it has to be prime"

paddic=3
z = []
for s in lst:
    cnt=0
    while (s%paddic==0):
        cnt+=1
        s/=paddic
    z.append(cnt)

print(z)

"This is to save all the p-adic values of the sequence in an array and show them"
"Thank you!"

