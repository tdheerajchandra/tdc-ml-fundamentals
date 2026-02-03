#!/usr/bin/env python
# coding: utf-8

# # Python-3

# ### Conditional Statements
# Conditional statements in Python are used to execute certain blocks of code based on specific conditions.<br>These statements help control the flow of a program, making it behave differently in different situations.<br> Generally we have 3 different types of Conditional statements: If,Elif,Else

# #### If:
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.<br>
# if *condition*:<br>
# &emsp; result of what should happen when the condition is true*<br>

# In[1]:


x=2
if x%2==0:
    print("Even")


# #### If Else:
# If condition is true the first block will be executed, if not the else condition will run.<br>
# if *condition*:<br>
# &emsp; statement when the condition is true<br>
# else:<br>
# &emsp; statement when the condition is false<br>

# In[3]:


x=int(input())
if x%2==0:
    print("Even")
else:
    print("Odd")


# #### If Elif Else:
# elif statement in Python stands for "else if." It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true.<br>
# if *condition1*:<br>
# &emsp; statement when the condition1 is true<br>
# elif *condition2*:<br>
# &emsp; statement when the condition2 is true<br>
# ...<br>
# else:<br>
# &emsp; statement when all the conditions are false<br>

# In[8]:


x=int(input())
if x>0:
    print("Number is Positive")
elif x<0:
    print("Number is Negative")
else:
    print("Number is Zero")


# The short form for the conditional statements can be written as: <br>
# *statement1* if *condition* else *statement2*

# In[11]:


x=int(input())
print("Even") if x%2==0 else print("Odd")


# In[14]:


marks=int(input("Enter the marks:"))
if marks<60:
    print("F grade")
elif 60<marks<70:
    print("D grade")
elif 70<marks<80:
    print("C grade")
elif 80<marks<90:
    print("B grade")
else:
    print("A grade")


# In[18]:


fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit=input("Enter a fruit name:")
if new_fruit in fruits:
    print("It is already in the list")
else:
    fruits.append(new_fruit)
    print(fruits)


# In[24]:


person={'first_name': 'Arjun', 'last_name': 'Sarkar', 'age': 37, 'country': 'India',
'is_married': False, 'skills': ['NodeJS', 'React', 'MongoDB', 'Python', 'SQL']}
if person['skills']:
    print(person['skills'][int(len(person['skills'])/2)])
if "Python" in person['skills']:
    print(True)
if person['is_married']==True:
    print("Arjun is married")
else:
    print("Arjun is not married")


# ### Loops
# In programming we also do lots of repetitive tasks. In order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops:<br>
# 1) For loop
# 2) While loop

# #### For loop:
# A for keyword is used to make a for loop, similar with other programming languages, but with some syntax differences. Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).<br>
# for *iterator* in *variable/data type*:<br>
# &emsp;*statements* 

# In[30]:


num=[0,1,2,3,4,5]
for i in num:
    print(i,end=' ')


# In[31]:


name="Dheeraj"
for j in name:
    print(j,end='.')


# In[42]:


dict1={'name':'Dheeraj','age':25,'sex':'Male','location':'Mumbai'}
for i in dict1.keys():
    print(i,end=" ")
for j in dict1.values():
    print(j,end=" ")
for k in dict1.items():
    print(k,end=' ')


# #### While Loop:
# It is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the lines of code after the loop will be continued to be executed.<br>
# while *condition*:<br>
# &emsp;*statements*

# In[45]:


x=0
while x<5:
    print('Hello')
    x+=1
else:
    print(x)


# #### Break, Continue & Pass:
# Break: We use break when we like to get out of or stop the loop.<br>
# Continue: With the continue statement we can skip the current iteration, and continue with the next.<br>
# Pass: In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.

# In[55]:


num=[i for i in range(1,11)]
for i in num:
    if i==8:
        break
    if i==5:
        print("Special number:5",end=" ")
        pass #For future spacegholder
    if i%2==0:
        continue
    print(i,end=" ")


# In[59]:


num=[i for i in range(1,101)]
even_res,odd_res=0,0
for i in num:
    if i%2==0:
        even_res+=i
    else:
        odd_res+=i
print("The sum of even numbers is:",even_res)
print("The sum of odd numbers is:",odd_res)


# In[64]:


fruits=['banana', 'orange', 'mango', 'lemon','apple']
i,j=0,len(fruits)-1
while i<j:
    fruits[i],fruits[j]=fruits[j],fruits[i]
    i+=1
    j-=1
print(fruits)


# ### Functions
# A function is a reusable block of code or programming statements designed to perform a certain task.<br>To define or declare a function, Python provides the def keyword.<br> Functions can be declared with or without parameters.<br>
# <b>def *function_name*(*parameters*):<br>
# &emsp;*statements*<br>
# function_name() #Calling the function</b><br>
# *Note:* When you use return in the function, while calling the function use print. Else just use the function name.

# In[67]:


#Function call with parameters
def area(l,w):
    print(l*w)
area(10,2)
#Function call without parameters
def volume():
    l=10
    w=3
    h=2
    return(l*w*h)
print(volume())


# #### Passing arguments with Key Value pairs
# Mandatory (no default) arguments must come first, and optional (default) arguments must come after them.

# In[73]:


def name(first,last):
    full_name= first+" "+last
    return(full_name)
print(name(first="Dheeraj",last="T"))

#Function with default parameters
def name(last,first="Dheeraj"):
    full_name=first+" "+last
    return(full_name)
print(name("T"))
print(name("T","Suraj"))


# #### Arbitary number of arguments
# Sometimes we don't know how many number of arguments will be there in function. In that case we will use \* before the parameter

# In[80]:


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(1,2,3,4,5))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-IND','MSD','VK','RS','RP')


# #### List Comprehensions & Lambda Functions
# *List comprehension* is a short way to create a new list.<br>It is considerably faster than processing a list using the for loop.<br>[*expression* for i in *iterable* if *condition*]<br>
# *Lambda function* is a small anonymous function without a name.<br>It can take any number of arguments, but can only have one expression.<br>To create a lambda function we use lambda keyword followed by a parameter(s), followed by an expression<br> lambda *parameters*:*expression/statement*

# In[88]:


l=[i for i in range (1,11)]
print(l)
res=lambda a,b:a+b
print(res(2,3))
print((lambda a,b,c:(a*a)-(b*b)+(c*c))(2,3,4))

