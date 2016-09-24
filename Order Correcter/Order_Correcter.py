import re

s=''
prev=''
dic={}
d2={}
ptrn = re.compile("[Q][1-8][)]")

f = open('Python_Assignment.txt', "r")
for line in f:
    s=s+line
f.close()

for m in ptrn.finditer(s):
    dic[ m.group() ] = int( m.start() )
    d2[prev] = int( m.start() )
    prev = m.group()
d2[prev] = len(s)-1

f2 = open('Python_Assignment_corrected.txt', "w")
f2.write(s[:ptrn.search(s).start()-1])
for y in range(1, 9):
    ste="Q%d)" %(y)
    f2.write('\n')
    f2.write(s[dic[ste]:d2[ste]-1])

f2.close()