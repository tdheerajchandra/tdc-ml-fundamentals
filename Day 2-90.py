#!/usr/bin/env python
# coding: utf-8

# # Python - 2

# ### Lists

# Lists are a built in data type that allows to store multiple items in a single variable <br>
# They are heterogeneous, mutable, ordered and allows duplicates <br>
# Ordered: They are stored in the same order in the way the data is fetched and read <br>
# *Note:* Since they are indexed, they allow duplicates in them <br>

# In[2]:


thelist=['a','b','c']
print(thelist)


# List consturctor can also be used to create a list<br> Syntax is list()

# In[4]:


thelist=list(['a',1])
print(thelist)


# #### List Modification

# The elements in the list can be modified by accessing the list items using indexes<br>
# Just like the strings, lists also have indexes starting from 0 to n-1 from left to right and -1 to -n from right to left

# In[7]:


movies=['RS','DHU','NNNM','AK2','BMW']
print(movies)
print(movies[1])
movies[1]='AOR'
print(movies)
print(movies[-2])
movies[-2]="MSVPG"
print(movies)


# Multiple items in a list can be changed by using slicing technique

# In[20]:


ipl=['CSK','MI','RCB','RPS','KTK','PBKS','DC','GT','SRH']
print(ipl)
ipl[3:5]=['LSG','KKR']
print(ipl)
iplwin=ipl[0:3]+ipl[-2::1]
print(iplwin)
# Even KKR won an IPL trophy but there is a catch
print (type(ipl[4])) #str
# It returns a single string element but a string cannot be concatenated directly to a list
# So we use split inbuilt function to convert it into a list
iplwin=ipl[0:3]+ipl[-2::1]+ipl[4].split()
print(iplwin)


# *in* is used to verify whether the element is present in the list or not

# In[26]:


ipl=['CSK','MI','RCB','RPS','KTK','PBKS','DC','GT','SRH']
if "KKR" in ipl:
    print(True)
else:
    print(False)


# #### Some common functions in Lists <br>
# len(): To tell the length of the list<br>
# append(): To add the elements into the list at the end<br>
# insert(): To add the elements into the list at a particular index/position<br>
# pop(): To remove the end element from the list<br>
# remove(): To remove the element from a particular position from the list by accessing the item without index<br>
# del(): To remove the element from a particular position from the list by accessing the item with only index<br>
# clear(): To remove all the elements and just keep the list<br>
# extend(): That joins the one list to another list<br>
# count(): To find the number of occurance of an element<br>
# sort(): To sort the items in the list in and order<br>
# copy(): To create a duplicate list<br>
# The below example explains how copy function works

# In[28]:


dir=['east','west','north','south']
dir1=dir
dir2=dir.copy()
dir.pop()
print(dir,dir1,dir2)


# #### A small challenge with all the list functions

# In[43]:


guests = ["Ram", "Shyam", "Ram", "John","Vardhan","Krish","Guru","Nandan"]
print(guests)
print(len(guests))
#Adding a new guest named "Shiva"
guests.append("Shiva")
print(guests)
#Insert Bheem at Index 1
guests.insert(1,"Bheem")
print(guests)
#Vardhan cancelled his plan so remove him from the list
guests.remove("Vardhan")
print(guests)
#Because of Vardhan cancelled, Shiva also cancelled his plan
guests.pop()
print(guests)
#Feels like there are 2 Ram's in the list, find it out
print(guests.count("Ram")) #2
#Yeah there are 2 Ram's in the list, remove one of the Ram
guests.remove("Ram")
print(guests)
#Bheem name was entered in the wrong list so let's remove him
ind=guests.index("Bheem")
print(ind)
del guests[ind]
print(guests)
#Let's make it a copy so that it will be as a backup
backup_guests=guests.copy()
#Let's extend this list with the new batch
guests.extend(['Varun','Hemanth','Sathwik'])
#Let's sort the list
guests.sort()
print(guests)


# ### Tuples

# A primitive data type in python which are immuatble and ordered in nature which doesn't allow duplicates in them

# In[44]:


x=tuple(('apple'))
y=tuple(('apple',))
z=tuple(('apple','banana'))
print(x,y,z)


# Tuples are immutable in nature, but to make changes in a tuple data, change it to a list then perform operations on it and then change it to a tuple again<br>
# Tuple is defined in a simple braces and with the keyword *tuple(())*<br>
# Two tuples can be concatenated by using + operator

# In[52]:


x=('apple','banana')
y=list(x)
y.append('guava')
print(y)
x=tuple((y))
print(x)
z=tuple(("orange",))
print(x+z)


# count(): To count the number of times an element occured in the tuple<br>
# index(): To find the position of the element in the tuple<br>
# del: To remove the element in a tuple <br>
# Indexing: They support positive and negative indexing as list and string

# #### Exercise on Tuples

# In[60]:


sisters=tuple(("Jani","Teju","Sunu"))
brothers=tuple(("Suman","Nithish","Nani"))
siblings=sisters+brothers
print(len(siblings))
family_members=(('Krishna','Sujatha'))+siblings
print(family_members)


# ### Sets
# *Set* is a collection of unordered and un-indexed distinct elements. It means it doesn't allow duplicates in them<br> In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.<br>Syntax to create a set is Set() and sets are defined in curly braces

# len(): To find length of set <br>
# add(): To add a single element into the set<br>
# update(): To add multiple elements into the set<br>
# pop(): To remove the last element in the set<br>
# remove(): To remove the desired element from the set<br>
# clear(): To empty the entire set<br>
# del: To just remove the entire set<br>
# *clear vs del:* Clear just removes the data in the set which leaves the set to be empty where as del just deletes the set itself<br>
# Set to list conversion can be done using list(set_name) and can perform operations<br>

# In[68]:


sauce={'White','Red','Pink'}
#Add a new sauce named Pesto
sauce.add("Pesto")
print(sauce)
#Adding 2 more new sauces
sauce.update(['Green','Yellow'])
print(sauce)
#Yellow pasta doesn't exist so delete it out
sauce.pop()
print(sauce)
#Creating a new set pasta
pasta={'Penne','Spaghetti','Risotto'}
#Currently we don't need pasta types
pasta.clear()
print(pasta)
#Remove the pasta data also
del(pasta)


# #### Joining Sets
# There are several types of set joining methods <br>
# *Union:* A function that returns a new set with all the elements of set1 and set2. Syntax is .union() or | <br>
# *Intersection:* A function that returns a new set with the elements that are present in both the sets. Syntax is .intersection() <br>
# *Subset*: issubset()<br> *Superset*: issuperset()<br>
# *Difference*: A-B -> returns the elements of A which are not in B. B-A -> returns the elements of B which are not in A<br>
# *Symmetric Difference*: Returns all the elements of both sets, except the elements that are present in both the sets. Mathematically (A\B)U(B\A)
# *Disjoint*: When both the sets doesn't have any element in common, then they are called disjoint sets

# In[3]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Capgemini","TCS"])
print(it_companies)
it_companies.pop()
print(it_companies)
#Remove vs Discard: .remove() deletes the element and returns error if the element is not present in the set
#where as .discard() will not retrun an error if an element is not present in it
it_companies.discard("MuSigma") # Even though MuSigma is not in the set, it will not return any error
print(it_companies)


# In[10]:


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A|B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))


# ### Dictionary

# A dictionary is a collection of unordered, mutable paired (key: value) data type <br>
# A dictionary can be created using dict() or curly braces {} <br>
# Empty dictionary can be declared by using {}. <br>
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'} <br>
# *Length:* The length of the dictionary can be known by using len() function <br>
# *Accessing an element in Dict:* print(dct[key_1]). If the key doesn't exist, then while accessing it will return an error <br>
# *Adding items*: Items can be added into the dict using dct[key]="value"<br>
# *Modifying items*: Just like adding items, we can also modify just in the same way dct[key]='value'<br>
# *pop:* pop(key) will remove the value for which the given key is associated. popitem() will remove the last item of the dictionary. del: removes an item with specified key name

# In[19]:


ipl={"MI":5,"CSK":5,"KKR":3,"RCB":1}
print(len(ipl))
print(ipl["CSK"])
ipl["SRH"]=0
print(ipl)
ipl["SRH"]=1
print(ipl)
ipl["KTK"]=0
print(ipl)
ipl.pop("KTK")
print(ipl)
ipl.popitem()
print(ipl)
del ipl["KKR"]
print(ipl)


# *.clear():* To clear the key:value pairs in the dictionary <br>
# *del*: To delete the entire dictionary<br>
# *.copy():* To copy the entire dictionary set without mutating one another<br>
# *.keys():* To return all the keys of a dictionary in a list<br>
# *.values():* To return all the values of a dictionary in a list<br>
