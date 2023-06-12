Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Interface for creating an object but letting subclasses decide which class to instantiate. It lets a class defer instantiation to subclasses.
**Also Known As:** Virtual Constructor

**Motivation**: Frameworks use abstract classes to define and maintain relationships between objects. A framework is often responsible for creating these objects as well. The Factory Method encapsulates the knowledge of which object subclasses to create and moves this knowledge of the framework.

**Use When**
- A class can't anticipate the class of objects it must create
- A class wants its subclasses to specify the objects it creates
- Classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

### Structure

![[Screenshot 2023-06-12 at 2.44.54 PM.png| 500]]

1. Product
		Defines the interface of objects the factory method creates
2. ConcreteProduct
		Implements the Product interface
3. Creator
		Declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.
		May call the factory method to create a Product object
4. ConcreteCreator
		Overrides the factory method to create a Product object

#### Collaborations
- Creator relies on its subclasses to define the factory method so that it returns an instance of the appropriate ConcreteProduct

### Consequences
Factory methods eliminate the need to bind application-specific classes into your code. The code only deals with the Product interface; therefore it can work with any user-defined ConcreteProduct classes.

A potential disadvantage of factory methods is that clients might have to subclass the Creator class just to create a particular ConcreteProduct object. Subclassing is fine when the client has to subclass the Creator class anyway, but otherwise the client now must deal with another point of evolution.

1. *Provides hooks for subclasses*: Creating objects inside a class with a factory method is always more flexible than creating an object directly. Factory Method gives subclasses a hook for providing an extended version of an object.
2. *Connects parallel hierarchies*

### Implementation
Consider the following issues when applying the Factory Method pattern:
1. *Two major varieties*: The two main variations of the Factory Method pattern are (1) the case when the Creator class is an abstract class and does not provide an implementation for the factory method it declares, and (2) the case when the Creator is a concrete class and provides a default implementation for the factory method. It's also possible to have an abstract class that defines a default implementation, but this is less common. The first case _requires_ subclasses to define an implementation, because there's no reasonable default. It gets around the dilemma of having to instantiate unforeseeable classes. In the second case, the concrete Creator uses the factory method primarily for flexibility. It's following a rule that says, "Create objects in a separate operation so that subclasses can override the way they're created." This rule ensures that designers of subclasses can change the class of objects their parent class instantiates if necessary.
2. *Parameterized factory methods*: Another variation on the pattern lets the factory method create _multiple_kinds of products. The factory method takes a parameter that identifies the kind of object to create.
3. *Language-specific variants and issues*
4. *Using templates to avoid subclassing*
5. *Naming conventions*

### Related Patterns
[[Abstract Factory]] is often implemented with factory methods. The Motivation example in the Abstract Factory pattern illustrates Factory Method as well. 

Factory methods are usually called within [[Template Method]]s.

[[Prototype]]s don't require subclassing Creator. However, they often require an Initialize operation on the Product class. Creator uses Initialize to initialize the object. Factory Method doesn't require such an operation.