#!/usr/bin/env python
# coding: utf-8

# # Day 1- Introduction to Python

# <b>Python</b> was introduced by *Gudio Van Rossum* in late 1980s and is basically a dynamically typed language unlike C, C++ which are statically typed language.<br>
# It uses Interpreter and this interpreter converts the code into a .pyc file which only runs in a system with Python Interpreter

# #### This is the first line of code which everyone teaches

# In[10]:


print("Hello World")


# #### The below are the basic mathematical operations that python supports

# In[12]:


print(3 + 4)   # addition(+)
print(3 - 1)   # subtraction(-)
print(6 * 6)   # multiplication(*)
print(4 / 3)   # division(/)
print(2 ** 3)  # exponential(**)
print(5 % 3)   # modulus(%)
print(3 // 2)  # Floor division operator(//)


# Python contains data types which are basically a classification that define the format, interpretation, and permitted operations of data stored in variables.<br> Python has Integer, Float, Imaginary and String as as primitive data types.<br>Apart from these it also has List,Set,Tuple and Dictionary as data types.

# In[13]:


print(type(10))                  # Int
print(type(3.143))                # Float
print(type(1 + 3j))              # Complex
print(type('Leonard'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Sheldon'}))  # Dictionary
print(type({9.8, 3.14, 1.6}))    # Tuple


# ### Variables

# A container that stores data which can be refered and can be maniputalted. <br> Variables are ofently started with alphabets and contains alphanumeric characters and numbers only.<br> In python, variables are need not to be declared before using like in C and C++. We can directly assign values to a variable without declaring it. <br> Python is also case sensitive.

# In[29]:


first_name= "Dheeraj"
last_name= "T"
age= 25
city= "Mumbai"
skills= ["UI5","FIORI","SAP Portal", "Python", "SQL"]
personal_info= {"Name":first_name+" "+last_name, "Age":age, "City":city, "Skills":skills}
print("Name:",first_name,last_name)
print("Age:",age)
print("City:",city)
print("Skills:",skills)
print("Personal Info",personal_info)


# #### Variables can also be declared in a single line

# In[32]:


first_name, last_name, age, city= "Sheldon", "Cooper", 30, "Los Angeles"
print(f"My name is {first_name} {last_name} and I am from {city} of age {age}")


# ### Strings

# Any data type under single or double or triple quotes are known as *Strings*<br> There are different string methods and built-in functions to deal with string data types.

# In[33]:


letter = 'D'                # A string could be a single character or a bunch of texts
print(letter)               # D
print(len(letter))          # 1
greeting = "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13


# Strings can also be printed in multilines using triple quotes (can be single ' or double " quotes)

# In[34]:


multiline_string_1 = '''I always wonder about the sky
I really wonder what Astrophysics consists off.'''
print(multiline_string_1)

multiline_string_2 = """In the year 1983 team India has won it's first ICC World Cup
And again they won in the year 2011."""
print(multiline_string_2)


# <b>*String concatenation*</b> is a process of joining two or more strings

# In[36]:


first_name = 'Pradeep'
last_name = 'Ranganathan'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Pradeep Ranganathan
print(len(first_name))  # 4
print(len(last_name))   # 11
print(len(first_name) > len(last_name))  # False
print(len(full_name))  # 15


# <b>*Indexing:*</b> It is used in strings to access the characters in the string <br> Indexing in strings starts from 0 to n-1 from left to right and from -1 to -n in reverse order (where n is the number of characters in a string) <br> <b>*Slicing:*</b> It is used to slice the string from one end to another end. <br>In simple terms, selecting a subset of sequential characters in a string.

# In[40]:


language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

sit_com = 'FRIENDS'
last_letter = sit_com[-1]
print(last_letter)  # S
second_last = sit_com[-2]
print(second_last)  # D

location = 'Mumbai'
# starts at zero index and up to 3 but not include 3
first_three = location[0:3]
last_three = location[3:6]
print(last_three)  # bai
# Another way
last_three = location[-3:]
print(last_three)   # bai
last_three = location[3:]
print(last_three)   # bai

# Skipping character while splitting Python strings
country = 'India'
jump = country[0:5:2]
print(jump)  # Ida


# #### There are lot of *String methods* in python<br>
# capitalize(): Converts the first character of the string to captial letter<br>
# count(): Retruns the occurence of the substring in the string *count(substring,start=...,end=...)*<br>
# find(): Returns the index of the first occurence of the substring<br>
# index(): Returns the index of substring<br>
# isalnum(): Checks alphanumeric character<br>
# isalpha(): Checks if all characters are alphabets<br>
# isdecimal(): Checks Decimal Characters<br>
# isdigit(): Checks Digit Characters<br>
# <b>*Note*</b>: None of these functions can determine whether a number is float/decimal or not<br>
# islower():Checks if all alphabets in a string are lowercase<br>
# isupper(): returns if all characters are uppercase characters<br>
# join(): Returns a concatenated string<br>
# strip(): Removes both leading and trailing characters (white spaces)<br>
# replace(): Replaces substring inside<br>
# split():Splits String from Left and returns in list format<br>
# title(): Returns a Title Cased String (uppercase of first letter in each word)<br>
# swapcase(): Exchanges the characters from lower to upper and vice versa<br>
# startswith(): Checks if String Starts with the Specified String<br>

# In[ ]:




