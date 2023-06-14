Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Decouple an abstraction from its implementation so that the two can vary independently.
**Also Known As:** Handle/Body

**Motivation**: When an abstraction can have one of several possible implementations, the usual way to accomodate them is to use inheritance. The Bridge pattern addresses this by putting abstraction and implementations in separate class hierarchies.

**Use When**
- Wanting to avoid a permanent binding b/w an abstraction and its implementation. For example, when the implementation must be selected or switched at run-time.
- Abstractions and their implementations should be extensible by subclassing. Bridge pattern lets you combine the different abstractions and implementations and extend them independently.
- Changes in the implementation of an abstraction should have no impact on clients
- You need nested generalizations of a proliferation of classes
- Want to share an implementation among multiple objects in a way which is hidden from the client.

### Structure

![[Screenshot 2023-06-13 at 12.48.16 PM.png| 500]]

1. Abstraction
		Defines the abstraction's interface
		Maintains a reference to an object of type Implementor
2. RefinedAbstraction
		Extends the interface defined by Abstraction
3. Implementor
		Defines the interface for implementation classes. It doesn't have to correspond exactly to Abstraction's interfaces.
4. ConcreteImplementor
		Implements the Implementor interface and defines its concrete implementation

#### Collaborations
- Abstraction forwards client requests to its Implementor objects

### Consequences
1. *Decoupling interface and implementation*: An implementation is not bound permanently to an interface. The implementation of an abstraction can be configured at run-time. Decoupling Abstraction and Implementor also eliminates compile-time dependencies on the implementation. Changing an implementation class doesn't require recompiling the Abstraction class and its clients.
2. *Improved extensibility*: You can extend the Abstraction and Implementor hierarchies independently.
3. *Hiding implementation details from clients*: You can shield clients from implementation details, like the sharing of implementor objects and the accompanying reference count mechanism

### Implementation
1. *Only one Implementor*: In situations where there's only one implementation, creating an abstract Implementor class isn't necessary.
2. *Creating the right Implementor object*: How, when, and where do you decide which Implementor class to instantiate when there's more than one? If Abstraction knows about all ConcreteImplementor classes, then it can instantiate one of them in its constructor; it can decide between them based on parameters passed to its constructor. If, for example, a collection class supports multiple implementations, the decision can be based on the size of the collection. A linked list implementation can be used for small collections and a hash table for larger ones. Another approach is to choose a default implementation initially and change it later according to usage. For example, if the collection grows bigger than a certain threshold, then it switches its implementation to one that's more appropriate for a large number of items.

### Related Patterns
An [[Abstract Factory]] an create and configure a particular Bridge.

The [[Adapter]] pattern is geared toward making unrelated classes work together. It is usually applied to systems after they're designed. Bridge, on the other hand, is used up-front in a design to let abstractions and implementations vary independently.