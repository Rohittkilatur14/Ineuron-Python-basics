#!/usr/bin/env python
# coding: utf-8

# ## Generators

# Generators are techniques which will create iterators from iterables.

# In[8]:


def getCubes(n):
  listOfSquares = []
  for i in range(n):
    listOfSquares.append(i**3)
    return listOfSquares


# In[9]:


getCubes(5)


# In[19]:


def genCubes(n):
    for num in range(n):
      yield num**3


# In[20]:


output = genCubes(5)
output


# In[21]:


for i in output:
    print(i)


# In[24]:


def genfibon(n):
    ''''''
    ##Generate a fibonacci series upto n
    
    ''''''
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


# In[31]:


a = list(genfibon(10))


# In[32]:


a


# In[33]:


for i in list(genfibon(10)):
    print(i)


# Map is basically used to apply any sort of functions to any number of elements in a list rather than a single value for a single variable 

# In[35]:


def square_num(x):
    return x*x


# In[37]:


a = square_num(5)


# In[38]:


a


# In[44]:


a = list(map(square_num,[1,2,3,4,5]))


# In[45]:


a 


# In[72]:


def fahrenheit(T):
    return((float(9)/5)* (T+32)
       
           
           
def celsius(T):
        return((float(5)/9)* (T-32))
                          
                      
           
def summ(x,y):
           return x+y


# In[75]:


def fahrenheit(T):
    return((float(9)/5)* (T+32))
           
         
       


# In[77]:


fahrenheit(32)


# In[78]:


temp = [0,22.5,40,100]


# In[80]:


list(map(fahrenheit,temp))


# ## Lambda Function

# Lambda is a function without any function name and without using any function, I can process whatever element I want

# In[81]:


list(map(lambda x:x**2,[1,2,3,4,5,6]))


# In[90]:


list(map(lambda x: (((9)/5)*x + 32),temp))


# In[88]:


list(map(lambda x: (float(5)/9)* (x-32),[1,2,3,4,5,6]))


# ## Lambda without map()

# In[91]:


a = lambda x:x**2


# In[96]:


a(5)


# In[102]:


a = lambda x,y:(x*2,y*2)


# In[103]:


a(5,6)


# In[98]:


a = lambda x,y:(x+y,x-y)


# In[99]:


a(2,3)


# ## reduce()

# We keep reducing the sequence of elements to a single digit by doing one-on-one addition taking 2 elements at a time.

# In[ ]:


from functools import reduce
reduce()


# In[108]:


max_find = lambda a,b: a if (a>b) else b


# In[109]:


max_find(23,45)


# In[124]:


max_find = lambda a,b: a if (a>b) else b
list = [45,43,56,78]


# In[125]:


reduce(max_find,list)


# In[112]:


sum_res = lambda a,b: a+b
list = [23,4,5,67]


# In[113]:


reduce(sum_res,list)


# In[138]:


tuple(map(lambda x,y : 9/5*x+32,[1,2,3,4],[2,3,4,5]))


# ## filter()

# This function offers a convenient way to filter out all the elements of a variable by which the function returns 'true'

# In[115]:


def even_check(num):
    if num%2 == 0:
        return True
        


# In[118]:


filter(even_check,list)


# In[129]:


list = [1,2,3,4,5,6,7,8,9,10]
tuple(filter(even_check,list))


# In[132]:


tuple(map(lambda x:x%2==0,list))


# ## Nested Lambda():

# In[133]:


square = lambda x : x**2
product = lambda f, n: lambda x: f(x)*n

ans = product(square,2)(10)
print(ans)


# In[ ]:




