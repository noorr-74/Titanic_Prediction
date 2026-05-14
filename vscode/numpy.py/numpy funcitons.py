import numpy as np
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(np.exp(a))
print(np.max(a))
print(np.min(a))
#mathmateical functions:np.sqrt,np.sin,np.cos,np.tan,np.log
#aggregate functions: a.sum,a.max,a.min,
#statistics functions:a.mean,np.median,np.std,a.transpose()

b=np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]

])#items=12

b=b.reshape((2,6))#in reshape you should keep the same number of items
#items=12 
b=b.reshape((2,3,2))
print(b)

print(b.flatten())#outputs the matrix in 1d mat(vector)

a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])



b=np.array([
    [1,2,3,],
    [4,5,6,],
    [7,8,9,]

])




c=np.concatenate((a,b))
print(c)#concatenate make them a merged mat
c2=np.stack((a,b))
print(c2)#stack make them seperated
c3=np.split(a,3)#split the matrix into 4 arrays

a=np.append(a,b,axis=0)
print(a)
a=np.insert(a,2,b,axis=0)


