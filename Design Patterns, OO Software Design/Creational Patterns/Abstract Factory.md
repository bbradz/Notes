Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Interface for creating families of related or dependent objects w/o concrete classes.
**Also Known As:** Kit

**Motivation**: Use an Abstract class to provide a unified Interface which any client can use to produce many different concrete implementations of that Abstract class w/o needing to know what those concrete implementations are.

**Use When**
- A system should be independent of how its products are created, composed, and represented
- A system should be configured with one of multiple families of products
- A family of related objects is designed to be used together, and you need to enforce this constraint
- You want to provide a class library of products, an you want to reveal just their interfaces, not their implementations

### Structure

![[Screenshot 2023-06-12 at 1.26.34 PM.png| 600]]

- AbstractFactory
	- Declares an interface for operations that create abstract product objects
- ConcreteFactory
	- Implements the operations to create concrete product objects
- AbstractProduct
	- Declares an interface for a type of product object
- ConcreteProduct
	- Define a product object to be created by the corresponding concrete factory
	- implements the AbstractProduct interface
- Client
	- uses only interfaces declared by AbstractFactory and AbstractProduct classes

#### Collaborations
- Normally a single instance of a ConcreteFactory class is created at run-time. This concrete factory creates product objects having a particular implementation. To create different product objects, clients should use a different concrete factory
- AbstractFactory defers creation of product objects to its ConcreteFactory subclass

### Consequences
1. It isolates concrete classes
2. It makes exchanging product families easy
3. It promotes consistency among products
4. Supporting new kinds of products is difficult

### Implementation
1. Factories are Singletons: 
		Only one instance of a ConcreteFactory per product family is needed
2. Creating the Product
		AbstractFactory only declares an _interface_ for creating products. It's up to ConcreteProduct subclasses to actually create them. The most common way to do this is to define a factory method ([[Factory Method]]) for each product. A concrete factory will specify its products by overriding the factory method for each. While this implementation is simple, it requires a new concrete factory subclass for each product family, even if the product families differ only slightly.
3. Defining 
		AbstractFactory usually defines a different operation for each kind of product it can produce. The kinds of products are encoded in the operation signatures. Adding a new kind of product requires changing the AbstractFactory interface and all the classes that depend on it.
		A more flexible but less safe design is to add a parameter to operations that create objects. This parameter specifies the kind of object to be created. It could be a class identifier, an integer, a string, or anything else that identifies the kind of product. In fact with this approach, AbstractFactory only needs a single "Make" operation with a parameter indicating the kind of object to create. This is the technique used in the Prototype- and the class-based abstract factories discussed earlier.

### Related Patterns

AbstractFactory classes are often implemented w/ factory methods ([[Factory Method]]) but they can also be implemented using [[Prototype]]

A concrete factory is often a singleton ([[Singleton]])