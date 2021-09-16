# OOP-In-Python
This repo will serve as a quick-reference for anything Python OOP related

## What is an object and what does it mean to be object-oriended?
Objects are something we are all familiar with whether that be a wooden block when we were young or our phone now.
Certain objects are used for certain purposes: phones call people, bells ring, and buttons are pressed. 
An object in software is not all that much different. 
Software object are not tangible but are models of something that can do certain things and have certain things done to them.
Formally, an object is a collection of **data** and associated **behaviors**.

To be _oriented_ towards something means to be _directed towards_ it.
Object-oriented programming means programming that is directed towards modeling objects.
It is
defined by describing a collection of interacting objects via their data and behavior.

## What is a class?
Classes are used to differentiate objects. Apples and oranges are both objects, but we all know they are not the same. 
In object-oriented modeling, the term used for a _kind of object_ is **class**.
If we were to create an inventory application for a fruit farm we would need a class for apples and a class for oranges.
Classes describe objects. They are like blueprints for creating an object.
You might have three apples sitting on a table in front of you.
Each apple is a distinct object, but all three have the attributes and behaviors associated with one class: the general class of apples.

## What is UML?
UML stands for Unified Modeling Language and is used to diagram different parts of object-oriented modeling. 
It can be used to diagram class and object diagrams, use cases, deployment, state changes, and more.

## What does data and associated behaviors refer to within an object?
Above we noted that _an object is a collection of data and associated behaviors_.
In this section we will dive into what _data_ and _behaviors_ specifically refer to.

### Data
Data represents the individual characteristics of a certain object.
A class can define specific sets of characteristics that are shared by all objects from that class.
Any specific object can have different data values for the given characteristics.
For example, the three apples on our table could each weigh a different amount.
The apple class could have a weight attribute to represent that characteristic.
All instances of the apple class have a weight attribute, but each apple has a different value for this attribute.
Attributes don't have to be unique, though; any two apples may weigh the same amount.
Attributes are frequently referred to as members or properties when it comes to object-oriented modeling.
When it comes to Python, members and properties can be used interchangeably.

### Behaviors
Behaviors are actions that can occur on an object.
The behaviors that can be performed on a specific class of object are called **methods**.
At the programming level, methods are very similar to functions, but they _magically_ have access to all the data associated with this object.
Like functions, methods can also accept **parameters** and return **values**. 

A method's parameters are provided to it as a list of objects that need to be passed into that method.
The actual object instances that are passed into a method during a specific invocation are usually referred to as arguments.
In Python, the first argument to almost all methods is the current object the method is being invoked on.
For example, if the Apple class had a method **pick**, the first object passed into the method would be the apple object being picked.

## What is composition?
Composition is the act of collecting several objects together to create a new one.
Image we have a Car class.
This Car class may be made of an engine, body, and interior.
The act of collecting the engine, body, and interior objects into one object called a Car is composition.

## What is inheritance?
Inheritance describes the _is a_ relationship in programming. For instance, an apple _is a_ fruit.
An orange _is a_ fruit. Another way of thinking of it is inheritance is a family tree.
John Smith inherited his name from his father who inherited it from his father. 
Instead of inheriting physical featured and behaviors from a person, one class can inherit attributes and methods from another class.

In our example above every fruit needs an expiration date.
Therefore, we could model this by creating a Fruit class and giving it an expiration date attribute.
After this, both the Apple and Orange class would inherit from the Fruit class and by the nature of that inheritance, have an expiration date attribute.

## What is method overriding
Method overriding happens when a subclass provides a different implementation to an inherited method than the one found in the parent class.
For instance, let's say we have a Fruit class with a method **set_expiration_date** that sets the expiration date of a fruit to 10 days past the current day.
When creating the Orange class, we may want to change the implementation of the **set_expiration_date** method to have an orange expire after 20 days.
This can be accomplished by overriding the **set_expiration_date** method in the Orange class.
By doing this, when the Orange class uses the **set_expiration_date** method it will use the one in the Orange class instead of the one in the Fruit class.

## What is an abstract class?
An abstract class is a class with abstract methods. An abstract methods basically say this:
_We demand this method exist in any non-abstract subclass, but we are declining to specify an implementation in this class._

## What is an interface?
An interface is a class that does not implement any methods at all.
The purpose of an interface is to tell a subclass what to do without providing and implementation for how to do it

## What is polymorphism?
Polymorphism is the ability to treat a class differently, depending on which subclass is implemented.
Pretend we have an Apple class that inherits from a Fruit class.
If we create an Apple object that object can be treated as either a Fruit or an Apple.
Because Apple inherits from Fruit, the object is both a Fruit and Apple.
This can be helpful with different layers of abstraction. 

For instance, let's say the Fruit class has a **set_expiration_date** method that sets the expiration date of a fruit to 10 days past the current day.
Different subclasses of Fruit can override this **set_expiration_date** method to set custom expiration date times.
When picking the fruit, we can simply call the **set_expiration_date** method on all Fruit objects no matter what type of fruit they are.
This is because all fruit classes that we define will inherit from the Fruit class and therefore all have a **set_expiration_date** method.