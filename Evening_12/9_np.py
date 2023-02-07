#################################################
#  09.12.2022 09.00 AM
#################################################
#  TOPICS TO BE COVERED
# 👉 NUMPY
# https://numpy.org/doc/stable/user/quickstart.html
#################################################
import numpy as np

z = np.zeros([5,3])
print(z)

o = np.ones([5,3])
print(o)

d = np.eye(5)
print(d)

# a =  np.arange(10,50,5).reshape(3,3)
# print(a)
# print(a.ndim)
# print(a.size)

a =  np.arange(10,51,5)
print(a)
print(a.ndim)
print(a.size)

s = np.linspace(10,51,5)
print(s)
print(s.size)


# printing arrays 

a = np.arange(18).reshape(6,3)
print(a)


# BASIC operations on array 

# a = np.arange(10,50,5).reshape()
a = np.linspace(10,50,9).reshape(3,3)
b = np.linspace(50,100,9).reshape(3,3)

print(a)
print(b)
print("**BASIC operations on array **")
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# universal functions

print(np.sqrt(a))

#unary operation
print(a.min())
print(a.max())
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a.min(axis=0))
print(a.min(axis=1))
print(a.max(axis=0))
print(a.max(axis=1))


from numpy import pi
x1 = np.linspace(0, 2 * pi, 50)
f = np.sin(x1)
print(f)


# import plotly.express as px
# fig = px.bar(x=list(range(50)), y=f)
# fig.write_html('first_figure.html', auto_open=True)
# print(fig)


# Indexing
# shape manipulation