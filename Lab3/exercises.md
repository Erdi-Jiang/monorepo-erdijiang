# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
    - *MObject is a concrete class. It is not declared as abstract, and it doesn't have any abstract methods (methods without implementation).*
      *In the main function, I created a MOject object without error, turning out it is a concrete class.*
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
    - *__del__ is a destructor method. It is called when an object is about to be destroyed and deallocated.*
    - *It is used for cleaning up resources or finalization before the object is removed from memory.*
1. What class does Texture inherit from?
	- *Class Texture inherits from Class Image, indicated by the line `class Texture(Image)`*
1. What methods and attributes does the Texture class inherit from 'Image'? 
    - *The class 'Texture' inherits all the methods and attributes of the 'Image' class.*
    - *It includes: constructor: `__init__`, methods: `getWidth()`, `getHeight()`, `getPixelColorR()`, `getPixels()`, and `setPixelsToRandomValue()`*
    - *Attributes like `m_wdith`, `m_height`, `m_colorChannels`, `m_Pixels`.*
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
    - *I think a texture has a 'has-a'(composition) relationship with image. Code refactored.*
    - *A 'Texture' is not a specialized type of 'Image'; rather, it is a different concept. While both 'Texture' and 'Image' may share some common attributes and methods related to pixel data and dimensions, they serve different purposes.*
    - *'Image' seems to represent a generic image with pixel data, while 'Texture' likely represents a texture that can be applied to 3D objects or used in computer graphics, which may involve additional properties and functionality.*
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
    - *Yes, Python automatically creates a constructor for class that does not declare a constructor.*
    - *Default constructor is called `__init__` and takes no arguments other than `self`.*

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
      -  `Logger created exactly once`
  - If the logger is already initialized, it will print:
      - `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

  
- *Code refactored*

2. Are singleton's in Python thread safe? Why or why not?

- *Current singleton's in Python is not thread safe. If multiple threads attempt to create an instance of the Logger class simultaneously, it's possible for more than one instance to be created because the check for cls._instance is None is not thread-safe.*
- *We can use `threading_lock` to make it thread-safe.*

*edit the code directly*  
  
