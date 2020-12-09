#!/usr/bin/env python
# coding: utf-8

# ## CONVERSION OF LIST INTO A TUPLE(Typecasting)

# In[1]:


tuple([1,2,4,3,5])


# In[3]:


type(tuple([1,2,4,3,5]))


# In[2]:


tuple([1,2,4,3,5,"Rohitt"])


# In[5]:


t=tuple([1,2,4,3,5,"Rohitt"])


# In[8]:


t


# ## Indexing

# In[11]:


t[5]


# ## Indexing of Strings in a Tuple

# In[10]:


t[5][2]


# In[7]:


tuple =(1,2,3,4,5)
print(tuple)


# In[8]:


type((1,2,3,4,5))


# In[ ]:


t =(1,2,3,4,5)


# In[12]:


t[1] = "Tata"
print(t)


# In[12]:


l = ['tom','rob','bob']


# In[13]:


l


# ## LIST INBUILT FUNCTIONS

# In[18]:


l.append("quick")


# In[19]:


l


# In[21]:


l.clear()


# In[22]:


l


# ## Copy an Object in Python
# In Python, we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. It only creates a new variable that shares the reference of the original object.
# 
# Let's take an example where we create a list named old_list and pass an object reference to new_list using = operator.
# 
# Example 1: Copy using = operator

# In[30]:


old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('New List:', new_list)


# Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:
# 
# Shallow Copy
# Deep Copy
# To make these copy work, we use the copy module.

# We use the copy module of Python for shallow and deep copy operations. Suppose, you need to copy the compound list say x. For example:

# import copy
# copy.copy(x)
# copy.deepcopy(x)
# 

# Here, the copy() return a shallow copy of x. Similarly, deepcopy() return a deep copy of x.

# ## Shallow Copy
# A shallow copy creates a new object which stores the reference of the original elements.
# 
# So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

# ## Example 2: Create a copy using shallow copy

# In[33]:


import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)


# To confirm that new_list is different from old_list, we try to add new nested object to original and check it.

# ## Example 3: Adding [4, 4, 4] to old_list, using shallow copy

# In[34]:


import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)


# However, when you change any nested objects in old_list, the changes appear in new_list.

# ## Example 4: Adding new nested object using Shallow copy

# In[35]:


import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)


# In the above program, we made changes to old_list i.e old_list[1][1] = 'AA'. Both sublists of old_list and new_list at index [1][1] were modified. This is because, both lists share the reference of same nested objects.
# 
# 
# 

# ## Deep Copy
# A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
# 
# Let’s continue with example 2. However, we are going to create deep copy using deepcopy() function present in copy module. The deep copy creates independent copy of original object and all its nested objects.

# ## Example 5: Copying a list using deepcopy()
# 

# In[36]:


import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)


# In the above program, we use deepcopy() function to create copy which looks similar.
# 
# However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.
# 
# 

# ## Example 6: Adding a new nested object in the list using Deep copy

# In[37]:


import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)


# In the above program, when we assign a new value to old_list, we can see only the old_list is modified. This means, both the old_list and the new_list are independent. This is because the old_list was recursively copied, which is true for all its nested objects.

# ## String Reversal

# In[14]:


[i[::-1]for i in l]


# ## Item Reversal 

# In[15]:


[i[::-1]for i in l][::-1]


# ## To Skip last element

# In[16]:


[i[::-1]for i in l][:-1]


# ## Python List extend()

# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.

# The syntax of the extend() method is:

# In[49]:


list1.extend('iterable')


# # Return Value from extend()

# The extend() method modifies the original list. It doesn't return any value.
# 
# 

# ## Example 1: Using extend() Method
# 

# In[51]:


# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List:',  language)


# ## Example 2: Add Elements of Tuple and Set to List

# In[52]:


# language list
language = ['French']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
language.extend(language_tuple)

print('New Language List:', language)

# appending language_set elements to language
language.extend(language_set)

print('Newer Language List:', language)


# ## Other Ways to Extend a List

# You can also append all elements of an iterable to the list using:
#     

# ## 1. the + operator

# In[54]:


a = [1, 2]
b = [3, 4]

a += b    # a = a + b

# Output: [1, 2, 3, 4]
print('a =', a)


# ## 2. the list slicing syntax

# In[55]:


a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)


# ## Python extend() Vs append()
# If you need to add an element to the end of a list, you can use the append() method.
# 

# In[56]:


a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)


# # Set : 

# In[66]:


## set((tuple))
set((1,2,3,4,5))


# In[67]:


## set((List))
set([1,2,3,4,5])


# In[68]:


type(set([1,2,3,4,5]))


# In[72]:


list({1,2,3,4,5,6,7,3,4,2,5})


# In[73]:


{1,2,3,4,5,6,7,3,4,2,5}


# In[70]:


type({1,2,3,4,5})


# In[75]:


x = set()


# In[76]:


x


# In[77]:


x1 = {1,2,3,4,5}
x2 = {2,3,4,5,7,6}


# In[78]:


x1.add(6)


# In[79]:


x1


# In[80]:


x1.union(x2)


# In[81]:


x1.intersection(x2)


# In[82]:


x1.intersection_update(x2)


# In[83]:


x1


# In[85]:


x1.difference(x2)


# In[86]:


x1.difference_update(x2)


# In[87]:


x1


# In[88]:


x1.issubset(x2)


# In[89]:


x2.issuperset(x1)


# In[94]:


x2[2:]


# In[93]:


## Convert set to list so that indexing is possible
list(x2)[2:]


# In[95]:


x1 = {1,2,3,4,5,"Rohitt"}


# In[96]:


x1


# ## Dictionaries:
# 

# It is a combination of key value pairs

# In[97]:


type({})


# In[98]:


{1:"Rohitt",2:"Kilatur",3:29}


# In[99]:


var = {1:"Rohitt",2:"Kilatur",3:29}


# In[100]:


type(var)


# In[101]:


var.items


# In[102]:


var.items()


# In[103]:


var.items()[1]


# In[104]:


var.keys()


# In[105]:


var.keys()[1]


# ## Both Dict. keys and Values are not subscriptable, so convert into list for indexing

# In[108]:


list(var.keys())[1]


# In[109]:


{1:"Rohitt",2:"Kilatur",3:29,1:"Raman"}


# In[110]:


var.values()


# In[2]:


## In dict, indexing happens through keys
var = {1:"Rohitt",2:"Kilatur",3:29}


# In[3]:


var[1]


# In[4]:


var[3]


# In[5]:


mydict = {'key1':123,'key2':[12,23,45],'key3':['item0','item1','item2']}


# In[6]:


mydict['key2'][2]


# In[7]:


mydict['key3'][2]


# In[10]:


mydict['key3']


# In[11]:


type(mydict['key3'])


# In[15]:


mydict['key3'][2].upper()


# In[16]:


mydict['key3'][2].lower()


# In[17]:


mydict.keys()


# In[18]:


type(mydict.keys())


# In[19]:


mydict.values()


# In[20]:


type(mydict.values())


# In[21]:


mydict['key1']=mydict['key1']-123


# In[22]:


# Dict values are mutable
mydict


# In[27]:


mydict['key4']=24
mydict


# ## Nested Dictionary

# In[29]:


#Dict within a dict
d = {'key1':{ 'nestkey':{ 'subnestkey': 'value'}}}


# In[30]:


d


# In[31]:


d['key1']['nestkey']['subnestkey']


# In[32]:


d['key1']


# In[33]:


type(d['key1'])


# ## Dictionary Comprehension

# In[34]:


{x:x**2 for x in range (10)}


# In[47]:


#Adding element-to-element in 2 lists
lst1=[2,3,4,5,6,7]
lst2=[6,7,8,9,4,3]

res_list = [lst1[i] + lst2[i] for i in range(len(lst1))] 


# In[48]:


res_list

