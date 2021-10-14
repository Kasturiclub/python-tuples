#Tuple Items - Data Types
#Tuple items can be of any data type:

#Example
#String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)

#Example
#A tuple with strings, integers and boolean values:

tuple4 = ("abc", 34, True, 40, "male")
print(tuple4)
########################
#type()
#From Python's perspective, tuples are defined as objects with the data type 'tuple':

#<class 'tuple'>
#Example
#What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

####################

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.

#Example
#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)