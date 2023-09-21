# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*I agree that the names of member functions should correlate to what they do. Using suitable names so that reviewers can easily remember and understand the functionality, so that makes these functions easier to use. Other examples in the dictionary looks good are get(), keys(), values, items() and so on. Using "get" means get a single key and its value. keys() returns a list of keys in the dictionary instead of just one. So are the values() and items(). Update() is also another good verb describing the function.*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Dictionary are implemented using a hash table data structure, which are unordered collections of key and value pairs. Keys are unique and immutable.*
*Lists are implemented as dynamic arrays in Python. They are ordered with indexes that defautly starts from 0.*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes, in Python you can directly access any element in a list, if it exists in the list.*

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: It is flexible if a library supports any data types, meaning versatile. We do not need extra libraries to hold different data types if we have this one. The functions of this library can also be generic that works with different data types.*
*Cons: Since the library support different data types, it can lead to run time error if not be used correctly. It may be also confusing to get what the functions are doing if the data types are not specified.* 

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*The functions are well named that describe their actions clearly. Get(), post(), put(), delete() are based on http methods they correspond to.*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*The requests.Request() method takes lots of arguements in this one function. However, they often provide defaults or support the use of keyword arguments for clarity.*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*`**kwargs` allows user to pass a variable number of keyword arguments to the function. It's good for flexibility for users to customize without modifying signature. However, it also makes the code less explicit and harder to understand.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*`None`in the Session class serve as default values. If you do not spcify a value for the argument calling the method, it will use its default value - None. It balances between the flexibility and predictability.*
*Arguments can be set to other values different than `None`, depending on the behavior of the method. This is beneficial to allow users to modify specific aspects of the method's behavior.*
