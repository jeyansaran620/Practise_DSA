'''
  This will print the largest element formed by combining the array elements.  
'''
t=int(input())

while t>0:
    n=int(input())
    values=input().split()
   
    
    for x in range(0,len(values)-1):
        for y in range(x+1,len(values)):
            if int(values[y]+values[x]) > int(values[x]+values[y]):
                values[y], values[x] = values[x], values[y] 
    for x in values:
        print(x,end='')
            
    print('')
    t-=1