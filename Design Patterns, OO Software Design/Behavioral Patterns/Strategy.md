Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
**Also Known As:** Policy

**Motivation**: Instead of implementing algorithms where they are being used it may be better to allow flexible interchanging via defining classes that encapsulate different algorithms, that encapsulation being a strategy.

**Use When**
- Many related classes differ only in their behavior. Strategies provide a way to configure a class with one of many behaviors.
- You need different variants of an algorithm. For example, you might define algorithms reflecting different space/time trade-offs. Strategies can be used when these variants are implemented as a class hierarchy of algorithms.
- An algorithm uses data that clients shouldn't know about. Use the Strategy pattern to avoid exposing complex, algorithm-specific data structures.
- A class defines many behaviors, and these appear as multiple conditional statements in its operations. Instead of many conditionals, move related conditional branches into their own Strategy class.

### Structure

![[Screenshot 2023-06-14 at 12.48.50 PM.png| 500]]

1. Strategy
		Declares an interface common to all supported algorithms. Context uses this interface to call the algorithm defined by a ConcreteStrategy.
2. ConcreteStrategy
		Implements the algorithm using the Strategy interface.
3. Context
		Is configured with a ConcreteStrategy object.
		Maintains a reference to a Strategy object.
		May define an interface that lets Strategy access its data.

**Collaborations**: 
- Strategy and Context interact to implement the chosen algorithm. A context may pass all data required by the algorithm to the strategy when the algorithm is called. Alternatively, the context can pass itself as an argument to Strategy operations. That lets the strategy call back on the context as required.
- A context forwards requests from its clients to its strategy. Clients usually create and pass a ConcreteStrategy object to the context; thereafter, clients interact with the context exclusively. There is often a family of ConcreteStrategy classes for a client to choose from.

### Consequences
1. *Families of related algorithms* : Hierarchies of Strategy classes define a family of algorithms or behaviors for contexts to reuse. Inheritance can help factor out common functionality of the algorithms.
2. *An alternative to subclassing* : Encapsulating the algorithm in separate Strategy classes lets you vary the algorithm independently of its context, making it easier to switch, understand, and extend.
3. *Strategies eliminate conditional statements* : The Strategy pattern offers an alternative to conditional statements for selecting desired behavior. When different behaviors are lumped into one class, it's hard to avoid using conditional statements to select the right behavior. Encapsulating the behavior in separate Strategy classes eliminates these conditional statements.
4. *Choice of implementation* : Strategies can provide a choice of different implementations of the same behavior
5. *Clients must be aware of different Strategies* : Potential drawback in-that clients must understand how Strategies differ before it can select the appropriate one. 
6. *Communication overhead between Strategy and Context* : The Strategy interface is shared by all ConcreteStrategy classes whether the algorithms they implement are trivial or complex. Hence it's likely that some ConcreteStrategies won't use all the information passed to them through this interface; simple ConcreteStrategies may use none of it! That means there will be times when the context creates and initializes parameters that never get used. If this is an issue, then you'll need tighter coupling between Strategy and Context.
7. *Increased number of objects* : Strategies increase the number of objects in an application. Sometimes you can reduce this overhead by implementing strategies as stateless objects that contexts can share.

### Implementation
1. *Defining the Strategy and Context interfaces* : The Strategy and Context interfaces must give a ConcreteStrategy efficient access to any data it needs from a context, and vice versa. One approach is to have Context pass data in parameters to Strategy operations—in other words, take the data to the strategy. This keeps Strategy and Context decoupled. On the other hand, Context might pass data the Strategy doesn't need. Another technique has a context pass _itself_ as an argument, and the strategy requests data from the context explicitly.
2. *Making Strategy objects optional* : The Context class may be simplified if it's meaningful _not_ to have a Strategy object. Context checks to see if it has a Strategy object before accessing it. If there is one, then Context uses it normally. If there isn't a strategy, then Context carries out default behavior.

### Related Patterns
[[Flyweight]] : Strategy objects often make good flyweights