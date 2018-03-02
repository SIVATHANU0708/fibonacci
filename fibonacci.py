a=int(raw_input())
f1=0
f2=1
print(f2)
for i in range(2,a+1):
 f=f1+f2
 f1=f2
 f2=f
 print(f)
