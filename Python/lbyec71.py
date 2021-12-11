x=int(input("Input size of the array. "))
arr=[]
s=0
for i in range(0,x):
    variable=int(input("Input the variables in array. "))
    arr.append(variable)
    i+=1
for j in arr:
    s+=j
print(int(s))
  
