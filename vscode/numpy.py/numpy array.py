import numpy as np

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a[0])
print(b[0])
print(a+b)#[6,8,10,12]
w=np.random.random((4,5))#4 by 5 matrix with random numbers


c=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(c.shape[0])

x=[1,2,3,4]
y=[5,6,7,8]
print(x+y)#[1,2,3,4,5,6,7,8]

m=np.ones((2,5,3))
print(m)
l=np.full((2,4),5)
print(l)

x=np.arange(0,1000,5)#list from 0-1000 increses by 5

y=x*2 -x**2
print(y)

x=np.linspace(0,10,5)#list from 0-10 with 5 numbers& the steps is equal

a=np.array([

    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [10,20,30],
        [40,50,60]
    ]
],dtype=float)
print(a.shape)#(2,2,3)
print(a.ndim)#(3)
print(a.dtype)#int64

 

