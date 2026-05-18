# What can we do with python?
#1. Web development
#2. Data analysis
#3. Machine learning
#4. Artificial intelligence

#Syntax in python

# Which is the rules we have to follow when we write code in python
# 1. We have to follow indentation
# 2. We have to follow the syntax of python
# 3. We have to follow the rules of python  


print("Hello World")

name = "gigz"

age = 25 

#with names we use lowercase with underscores

person_name = "Karabo"

#can do camel case but not recommended

#Variables in python are case sensitive

"""Cannot contain the following characters:
- Spaces
- Special characters (except for underscores)
- Cannot start with a number  
- Cannot be a reserved keyword (like 'if', 'for', 'while', etc.)
- Cannot be the same as a built-in function name (like 'print', 'len', etc.)
- Cannot contain hyphens (-) or other special characters """

"""
Comment:

Comments are used to explain the code and make it more readable.

In Python, you can create comments using the following methods:

1. Single-line comments: Use the hash symbol (#) to create a single-line comment.

# This is a single-line comment

2. Multi-line comments: Use triple quotes to create multi-line comments.

'''
This is a multi-line comment.
It can span multiple lines.
'''
"""

#data types in python

#1. String  
#2. Integer
#3. Float
#4. Boolean
#5. List
#6. Tuple
#7. Dictionary
#8. Set
#9. None

#1. String: A sequence of characters enclosed in quotes (single, double, or triple).
name = "Karabo"
surname = "Magaga"
full_name = name + " " + surname # This is called string mnipulation, we are concatenating the name and surname to create a full name
print(full_name)

#Trple quotes can be used to create multi-line strings
long_string = """My name is Karabo,
my surname is Magaga"""
#
print(long_string)

#we can also repeat a string using the multiplication operator (*)
long_dash = "-" * 20
print(long_dash)

#we can also use the len() function to get the length of a string
number_of_dashes = len(long_dash)

print(number_of_dashes)

#We can add a variable to a string using the f-string (formatted string literals)

name = "john"

introduction = f"Hello, my name is {name}" #This is called string interpolation, we are inserting the value of the variable name into the string using the f-string syntax.

print(introduction)

#String Methods: Python provides a variety of built-in string methods that allow you to manipulate and work with strings in different ways. Some common string methods include:
# - upper(): Converts all characters in a string to uppercase.

full_name = "Karabo Magaga"

print(full_name.upper())
# - lower(): Converts all characters in a string to lowercase.

print(full_name.lower())

# - capitalize(): Converts the first character of a string to uppercase and the rest to lowercase.

print(full_name.capitalize())

# - strip(): Removes leading and trailing whitespace from a string.

whitespace_string = "   Hello, World!   "

print(whitespace_string.strip()) #This will remove the leading and trailing whitespace from the string, resulting in "Hello, World!".

# - replace(old, new): Replaces occurrences of a specified substring with another substring.

greeting = "Hello, World!"

print(greeting.replace("Hello", "Hi"))

# - split(separator): Splits a string into a list of substrings based on a specified

my_string = "Hello, World! Welcome to Python programming."

print(my_string.split(" ")) #This will split the string into a list of substrings based on the space character as the separator. The resulting list will be ['Hello,', 'World!', 'Welcome', 'to', 'Python', 'programming.']. The split() method can take any string as a separator, such as a comma, a period, or even a specific word. If no separator is provided, the default is to split on whitespace (spaces, tabs, and newlines).

my_bio = "Name: Karabo, Age: 25, Occupation: Software Developer"

print(my_bio.split(", ")) #This will split the string into a list of substrings based on the comma followed by a space as the separator. The resulting list will be ['Name: Karabo', 'Age: 25', 'Occupation: Software Developer']. This allows us to separate the different pieces of information in the bio based on the comma and space as the separator. The split() method is useful for parsing and extracting specific information from a string when you know the structure

#   separator.

#sepator can be any string, for example:

data = "Name: Karabo; Age: 25; Occupation: Software Developer"


# - join(iterable): Joins a list of strings into a single string using a specified

# my_joined_string = " | ".join(["Name: Karabo", "Age: 25", "Occupation: Software Developer"])  

#2. Integer: A whole number without a decimal point.

#Finding and Replacing Substrings: You can use the find() method to locate the position of a substring within a string, and the replace() method to replace occurrences of a substring with another substring.

my_string = "Hello, World! Welcome to Python programming."

print(my_string.find("World")) #This will return the index of the first occurrence of the substring "World" in the string, which is 7. If the substring is not found, it will return -1.

print(my_string.replace("World", "Universe")) 

# we can have booleans with methods as well, for example:

my_intro = "my name is karabo"

print(my_intro.startswith("my"))

print(my_intro.endswith("Magaga"))

#3. Integer: A whole number without a decimal point.

#We can perform arithematic operations with integers

x = 10
y = 15 
sum = x + y
print(sum)

"""
Order of operations: (PEMDAS)
1. Parentheses ()
2. Exponents
3. Multiplication *
4. Division /
5. Addition +
6. Subtraction -"""

#3. Boolean: Data type that can only take two values: true or false. used for conditional statements and logical operations, control the flow of a program, and make decisions based on certain conditions. 

is_raining = True
is_sunny = False

print(is_raining)
print(is_sunny) 

age = 25 

can_vote = age >= 18

print(can_vote)


"""
comparison operators:
- Equal to (==)
- Not equal to (!=)
- Greater than (>)
- Less than (<)
- Greater than or equal to (>=)
- Less than or equal to (<=)

""" 

#This comparison operators can be used to compare values and return a boolean result (True or False). They are commonly used in conditional statements (like if statements) to control the flow of a program based on certain conditions.

age = 25 
has_license = True 

#The and operator (and) returns True if both conditions are true, otherwise it returns False. we use it if there's more than one condition that needs to be met for a certain outcome to occur.

#for example

can_drive = age>=18 and has_license

print(can_drive)

power = 0


is_power_on = power == 1

print(is_power_on)

# The or operator (or) returns True if at least one of the conditions is true, otherwise it returns False. we use it when there's more than one condition that can lead to a certain outcome, and we want to check if at least one of those conditions is met.

is_weekend = True
is_holiday = False
can_relax = is_weekend or is_holiday

print(can_relax)

# The not operator (not) is a logical operator that negates the value of a boolean expression. It returns True if the expression is False, and it returns False if the expression is True. we use it when we want to check the opposite of a certain condition.

is_raining = True
is_not_raining = not is_raining
print(is_not_raining)

# The not operator can also be used to negate the result of a comparison or logical expression. For example:  
is_weekend = False
is_holiday = False
can_relax = not (is_weekend or is_holiday)
print(can_relax)  #In this example, the expression inside the parentheses (is_weekend or is_holiday) evaluates to False, and then the not operator negates that result, making can_relax True. This means that if it's not a weekend and not a holiday, then you can relax.

# Assignment operators:
# Assignment operators are used to assign values to variables. They include:

# - = (simple assignment)
name = "Karabo"

# - += (add and assign)

score = 10

#score after a try

score += 5 #This is the same as score = score + 5, is adding  5 to the cureent score and reassinging the new value to the variable name. the score will be 15 after this operation.

# - -= (subtract and assign)

egg_quantity = 15 

# after selling 3 eggs

egg_quantity -= 3 #This is the same as egg_quantity = egg_quantity - 3, is subtracting 3 from the current egg quantity and reassigning the new value to the variable name. The new value of egg_quantity will be 12 after this operation.

# - *= (multiply and assign)

investment_value = 100

# after a 10% increase

investment_value *= 1.10 #This is the same as investment_value = investment_value * 1.10, is multiplying the current investment value by 1.10 (which represents a 10% increase) and reassigning the new value to the variable name. The new value of investment_value will be 110 after this operation.

# - /= (divide and assign)

total_distance = 200

# after traveling for 4 hours

total_distance /= 4 #This is the same as total_distance = total_distance / 4, is dividing the current total distance by 4 (which represents the number of hours traveled) and reassigning the new value to the variable name. The new value of total_distance will be 50 after this operation, which represents the average speed in distance per hour.

#flow control statements: These are used to control the flow of a program based on certain conditions. They include:

# - if statements: Used to execute a block of code if a specified condition is true.  

name = "Karabo"
if name == "Karabo":
  print("Hello, KARABO!")

# - else statements: Used to execute a block of code if the condition in the if statement is false. don't have to specify a condition for the else statement, it will execute if the condition in the if statement is not met.

surmane = "Lebowa"

if surname == "Magaga":
  print("Hello, Magaga!")

else:
  print("Hello, stranger!")

# - elif statements: Used to check additional conditions if the condition in the if statement is false, before executing the else block. The eflif is useful when we have multiple options the code should check and provide actions for each option.

age = 25
if age < 18:
  print("You are a minor.")
elif age >= 18 and age < 65:
  print("You are an adult.")
else:
  print("You are a senior citizen.")

#flow for a lift

button_number = 6

if button_number == 0: 
    print("you are going to ground floor")
elif button_number == 1:
    print("you are going the first floor")
elif button_number == 2:
   print("you are going to the second floor")
elif button_number == 3:
   print("you are going to the third floor")
elif button_number == 4:
   print("you are going to the fourth floor")
else: 
   print("You haven't made your slection!")

#We also have nested if statements, which are if statements inside other if statements. They allow us to check multiple conditions in a hierarchical manner. They are useful when we have a situation where we need to check for multiple conditions that depend on each other.

has_license = True
type_of_license = "Driver's License"

if has_license: #The condition is true, so we go on to check other conditions that depend on this one being true. If this condition was false, we would skip the nested if statement and go to the else block.
   
   if type_of_license == "Driver's license":
      print("you can drive the car")
   else:
      print("You need supervison to drive the car")

else:
   print("You don't have a license, you cannot drive the car")

#loops: Used to repeat a block of code multiple times. They include:

# - for loops: Used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence.

#The syntax of a for loop is as follows:
# for variable in sequence:
#     # block of code to be executed

for i in range(5): #This will iterate over the numbers 0 to 4 (5 is not included) and execute the block of code for each number. This means when i is in the range of 5, print the value of i, but because python uses zero-based indexing, the loop will start with i = 0 and end with i = 4, resulting in a total of 5 iterations.

    #The i refers to the counter variable that takes on the value of each item in the sequence during each iteration of the loop. In this case, i will take on the values 0, 1, 2, 3, and 4 during the iterations of the loop.

    #The range refers to the built-in function range() that generates a sequence of numbers. In this case, range(5) generates the sequence of numbers from 0 to 4.

    print(i) #This will print "Hello World!" five times, once for each iteration of the loop. The variable i takes on the value of each number in the range(5) sequence during each iteration of the loop, but in this case, we are not using the variable i inside the loop, so it is just a placeholder.

# This code is explained as follows: The range(5) function generates a sequence of numbers from 0 to 4. The for loop iterates over each number in that sequence, assigning it to the variable i. Inside the loop, the print(i) statement is executed, which prints the current value of i to the console. As a result, this code will output the numbers 0, 1, 2, 3, and 4, each on a new line.

for i in range(2, 6): #This will iterate over the numbers 1 to 5 (6 is not included) and execute the block of code for each number. This means when i is in the range of 1 to 5, print the value of i, but because python uses zero-based indexing, the loop will start with i = 1 and end with i = 5, resulting in a total of 5 iterations.

    print(i) 

for i in range(1, 10, 2): #This will iterate over the numbers 1, 3, 5, 7, and 9 (10 is not included) and execute the block of code for each number. This means when i is in the range of 1 to 9 with a step of 2, print the value of i. The loop will start with i = 1 and end with i = 9, resulting in a total of 5 iterations.

    print(i)

#Data structure - use to store multiple values together in a single variable. They include:

#list: A collection of items that are ordered and changeable. Lists are defined using square brackets [] and can contain items of different data types.

my_list = ["Karabo", 25, True, 3.14]

#list are ordered, which means that the items in a list have a specific order and can be accessed using their index. The first item in a list has an index of 0, the second item has an index of 1, and so on.

#We can select items from a list using their index. For example, to select the first item in the list, we can use my_list[0], which will return "Karabo". To select the second item, we can use my_list[1], which will return 25. We can also use negative indexing to select items from the end of the list. For example, my_list[-1] will return 3.14, which is the last item in the list, and my_list[-2] will return True, which is the second to last item in the list

name = my_list[0]
print(name)
age = my_list[1]
print(age)
last_item = my_list[-1]
print(last_item)
second_last_item = my_list[-2]
print(second_last_item)

#We can aslo specify a range of items to select from a list using slicing. For example, my_list[1:3] will return a new list containing the items at index 1 and 2, which are 25 and True. The start index is inclusive, while the end index is exclusive.

sub_list = my_list[1:3]
print(sub_list)

#We can also use slicing with negative indices. For example, my_list[-3:-1] will return a new list containing the items at index -3 and -2, which are 25 and True. The start index is inclusive, while the end index is exclusive.

sub_list = my_list[-3:-1]
print(sub_list)

#We can also overwrite items from a list by assign a new value to a specific index.


my_list[0] = "Kmaster"
my_list[1] = 33 
my_list[2] = False
my_list[3] = 5.3

print(my_list)

#We can also add items to a list using the append() method, which adds an item to the end of the list.

my_list.append("CAR")

print(my_list)

# we can also insert an item at a specific index using the insert() method, which takes two arguments: the index where the item should be inserted and the item itself.

my_list.insert(1, "Magaga")

print(my_list)

#We can also remove items from a list using the remove() method, which removes the first occurrence of a specified item from the list.

my_list.remove("CAR")
print(my_list)

#python also has built-in functions that can be used with lists, such as len() to get the length of a list, sum() to get the sum of all items in a list (if they are numbers), and sorted() to get a sorted version of a list.

print(len(my_list))

#print(sum(my_list)) #This will raise an error because the list contains items of different data types, and the sum() function can only be used with numbers.

#e.g 

numbers = [5, 2, 9, 1, 5, 6]

# print(sum(numbers)) #This will return the sum of all the numbers in the list, which is 28. The sum() function takes the list of numbers and adds them together to return the total.

#print(sorted(my_list)) #This will raise an error because the list contains items of different data types, and the sorted() function can only be used with items that can be compared to each other (like numbers or strings).

#e.g

numbers = [5, 2, 9, 1, 5, 6]

print(sorted(numbers)) #This will return a new list containing the sorted numbers: [1, 2, 5, 5, 6, 9]. The sorted() function takes the list of numbers and returns a new list with the numbers arranged in ascending order.

#Dictionary - consist of key value pair

person = {
   "name" : "Karabo",
    "age" : 33,
    "city" : "Ekurhuleni"
}

print(person["city"])

person["name"] = "Magaga" #This is assigning the value "Magaga" to the key "name"

print(person["name"])

person["is_a_city"] = True #This is assigning the value True to the key "is_a_city"

print(person["is_a_city"])

del person["age"]

print(person)

#Dictionary Methods

#e.g

print(person.keys())

print(person.values())

print(person.items())

#updating multiple values in a dictionary

person.update ({"age":25, "name":"kmaster"})
print(person)

#Tupet is a data set is immutable

point = (10,5)

print(point[0])

#Sets make sure that there's no duplicate in the set

numbers = {1, 2, 3, 4,}

fruits = ["orange", "banana", "grapes","banana"]
print(fruits)
unique_fruits = set(fruits)
print(unique_fruits)

#add item

unique_fruits.add("pear")
print(unique_fruits)

#remove item

unique_fruits.remove("grapes")
print(unique_fruits)

#Check membership

if "grapes" in unique_fruits:
   print("grapes in the set")
else:
   print("Not part of the set")

print(type(unique_fruits))

#Building function 

#Function is a piece of code that can be reused.

#Defining the function

def greet():
   print("Hello, World!")
   print("my name is Karabo Magaga")

#For a function to be executed it must be called

greet()

#Syntax for functions

'''
1. Use lowercase letters
2. Seperate words with underscore
3. Be descriptive about what it does
'''

def check_weather():
   temperature = 26 
   if temperature > 25:
      print("It's hot outside")
   else: 
      print("The weather is nice outside")

check_weather()

#Parameters in the function are used to make the function more dynamic and customisable

def greet(name):
   print(f"Hello, {name}")

greet("Karabo")


def person_profile(name, age, city):

   print(f"my name is {name}, I am {age} years old and come from the city of {city}")

person_profile("Karabo", 33, "Ekurhuleni")

#Parameters are declared when defining the function inside the parentesis, and the argument or value is assigned when the function is called. The parameters in the parentesis must match with the arguments passed when calling the function.

def greet(name,surname):
   print(f"Hello, {name} {surname}")

greet(surname = "Magaga", name = "Karabo") #If we are explicit with assigning the the argument to the correct parameter the order doesn't mater

#we can set default values, meaning assign arguments to the parameters when defining the function, but the parameters that don't have default values need to be arranged first than those with default values.

def greet(name, surname = "Lebowa"):
   print(f"Hello, {name}, {surname}")

greet("Karabo", "Magaga")

#parameters together with argument allow to use variable in the function. to able to use the parameters in the function, should defined or declared when defining the function and the arguments for the parameters must be passed when calling the function.

def calculate_total(price,tax_rate,discount):
   tax = price * tax_rate
   final_price = price + tax - discount
   print(f"total_price: R{final_price}")

calculate_total(price = 100, tax_rate = 0.08, discount = 10)

# it is adversible that we map the argument with the parameters when calling the function to avoid errors in the programme.

#Local variable is a variable that is inside the function, can only be accessed and used within the function and cannot be used accessed outside the function

#e.g 

def person_profile(name, surname):

   age = 33 #This is a local variable

print(f"my full name is {name}{surname} and I am {age} years old")

person_profile(name = "Karabo", surname = "Magaga")

#Global variable is a variable that be accessed outside of the function but can be used in and outside the variable. 

age = 33 #This is a global variable

def person_profile(name, surname):

   print(f"my full name is {name} {surname} and I am {age} years old")

person_profile(name = "Karabo", surname = "Magaga")

#Return the results can be stored be used later

def add_return(a, b):

   return a + b
add_return(5, 5)

result = add_return(5, 5)

print(result)


def calculate_area(width, height):
   area = width * height 
   return area 

room_area = calculate_area(width = 5, height = 10)

print(room_area)

room_volume = room_area * 2

print(room_volume)

def simple_function():
   numbers = [1, 2, 3, 4, 5]
   first_number = numbers[0] #Code to be executed
   last_number = numbers[-1]  #Code to be executed
   return first_number, last_number #The reults of the excuted code stored in the return function, which we can say it is equivalent to function called because nothing will be return is the function is not called, therefore calling the function leads to something returned when code is executed.


f, l = simple_function()
result = simple_function() #Calling the function will result in the code excuted

print(f)
print(l)

print(result) 


#External tools

#Python's Ecosystem

#Build-in packages comes with python
#External needs to be installed with pip 

'''
1. module is a single python file.
2. package is a folder containing multipe python files.
3. Library is a collection of packages.
4. function is a block of code 
5. Class is a blueprint for creating objects.
'''

#Importing the package or modules

import math
math.sqrt(16) #we are using square root function in the math module

from math import sqrt,pi

square_root = sqrt(64)

print(square_root)

import random

number = random.randint(1, 10)

print(number)

choice = random.choice(["apple","banana","pear"])

print(choice)

import datetime

today = datetime.date.today()

print(today)

from datetime import datetime

now = datetime.now()

print(now) 

time_now = now.time()

print(time_now)

# Format: Hour:Minute:Second

print(now.strftime("%H:%M:%S")) 

print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

# Format as HH:MM:SS
formatted_time = now.strftime("%H:%M:%S")
print(formatted_time) # Example: 10:21:52

# Format as 12-hour clock with AM/PM
twelve_hour = now.strftime("%H:%M:%S %p")
print(twelve_hour) # Example: 10:21:52 AM

from datetime import datetime, timezone

utc_now = datetime.now(timezone.utc)
print(utc_now)

from datetime import datetime

# Get current time
now = datetime.now()

print(f"Current date and time: {now}")
print(f"Just the time: {now.strftime('%H:%M:%S')}")

import pytz
from datetime import datetime

# 1. Get current time in UTC (best practice)
utc_now = datetime.now(pytz.utc)

# 2. Convert UTC to a specific timezone
paris_tz = pytz.timezone("Europe/Paris")
paris_time = utc_now.astimezone(paris_tz)

print(f"Paris Time: {paris_time}")

import os

current_directory = os.getcwd()

print(current_directory)

#Package installation we use pip 

import pandas as pd

#requirement.txt is a file of package in a certain project. We don't have to do it manually we can use pip freeze > requirements.txt
#Requirements.txt file have the required lib for a certain project. can be installed into a project using pip install -r requirement.txt
#Pip free used to saves the libraries that have been used in a project on a requirements.txt file

#Find packages

#use GPT you aask for the exact package you can used, to a certain problem

#Working with API

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url) #API request
data = response.json() #API response with the data stored in a JSON file

print(data)

temperature = data["current"]["temperature_2m"]
print(temperature)

import requests

def get_weather (latitude, longitude):
   url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
   response = requests.get(url)
   data = response.json()
   temperature = data["current"]["temperature_2m"]
   return temperature

paris_temp = get_weather(latitude = 48.85, longitude = 2.35)
london_temp = get_weather(latitude = 51.51, longitude = -0.13)
tokyo_temp = get_weather(latitude = 35.68, longitude = 139.69)
Vosloorus_temp = get_weather(latitude = -26.358, longitude = 28.2075)
tafelkop_temp = get_weather(latitude = 25.046, longitude = 29.509)


print(f"Paris temperature: {paris_temp}")
print(f"London temperature: {london_temp}")
print(f"Tokyo temperature: {tokyo_temp}")
print(f"Vosloorus temperature: {Vosloorus_temp}")
print(f"Tafelkop temperature: {tafelkop_temp}")

#Thw pattern is the same when working with APIs

'''
1. You send a request to the API's URL with parameters(like coordinates)
2. The API processes your request abd find the data
3. You recieve JSON data back with the imformation
4. You can extract the specific parts of what you need from the data
'''





   








































      
 























