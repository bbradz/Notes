2023-05-30 @16:57

Status: #idea
Tags: [[Java OOP Guide]] [[𝑪𝑺 📍]] [[Pattern Name]]

- Patterns Catalog
- Vocab
- Common Causes of Redesign (w/ Patterns to help for each)

![[Screenshot 2023-05-30 at 5.17.53 PM.png| 350]] 
![[Screenshot 2023-05-30 at 5.18.45 PM.png| 350]]

## Patterns Catalog
---
#### Creational Patterns
Description: Abstract the instantiation system away from how its objects are actually composed and represented. It delegates instantiation instead of using inheritance to vary the class instantiated. Used to evolve towards object composition away from fixed inheritance. 

1. [[Abstract Factory]] : Interface for creating families of related or dependent objects w/o concrete classes.
2. [[Builder]] : Separate construction from its representation so that the process can create different representations.
3. [[Factory Method]] : Interface for creating an object, to defer instantiation to subclasses.
4. [[Prototype]] : Specify the kinds of objects to create in 1 interface, and create new objects from this prototype.
5. [[Singleton]] : Ensure a class only has one instance, and provide a global point of access to it.

#### Structural Patterns
Description: 

1. [[Adapter]] : Convert Interface of a class into another interface. Lets classes work together that couldn't otherwise.
2. [[Bridge]] : Decouple an abstraction from its implementation so that the two can vary independently.
3. [[Composite]] : Compose objects into trees to represent part-whole hierarchies which can be treated uniformly.
4. [[Decorator]] : Attach new responsibilities to an object. An alternative to subclassing for extending functionality.
5. [[Facade]] : Unified interface for subsystem interfaces. A higher-level interface to make subsystem more usable.
6. [[Flyweight]] : Use sharing to support large numbers of fine-grained objects efficiently.
7. [[Proxy]] : Provide a surrogate or placeholder for another object to control access to it.

#### Behavioral Patterns
Description: 

1. [[Chain of Responsibility]] : Have >1 object handle a request. Chain request objects in a object chain until handled.
2. [[Command]] : Encapsulate a request in an object to parameterize, queue, log, and operate on different requests.
3. [[Interpreter]] : Given a language, define its grammar and an interpreter for sentences in the language.
4. [[Iterator]] : Access the elements of an aggregate object sequentially w/o exposing underlying representation.
5. [[Mediator]] : Encapsulate how objects interact so they don't inter-refer, allowing independent varying interactions
6. [[Memento]] : Capture and externalize an object's internal state so it can be restored to this state later.
7. [[Observer]] : 1-to-many dependency b/w objects so that when one changes state, its dependents are updated.
8. [[State]] : Allow an object to alter its behavior when its internal state changes, appearing to change its class.
9.  [[Strategy]] : Define an algorithm family encapsulating each interchangeable. Allows independent algo variation.
10. [[Template Method]] : Define algorithm skeleton, having subclasses redefine steps within that skeleton
11. [[Visitor]] : A new operation to be performed on elements of an object structure w/o actually changing the classes

## Vocab
---
- **Signature:** An operation's name, parameters, and return value
- **Interface: **All the signatures in an object's operations
- **Type:** A name for a particular Interface
- **Subtype:** When an interface contains the interface of its super-type
- **Class:** An object's implementation
- **Instantiation:** Allocating storage for the object's internal data
- **Parent Class:** Defines all the data and operations which a subclass provides data to
- **Abstract Class:** Defining a common interface for its subclasses, un-instantiate-able
- **Mixin Class:** Provides an optional interface or functionality to other classes 
- **Delegate:** An object which contains operations for another object to request
- **Aggregations:** When one objects *owns* or is responsible for another
- **Acquaintance:** When one objects *knows of* another object

## Common Causes of Redesign
---
1. **Creating an object by specifying a class explicitly:** 
	``Specifying a class name when You create an object commits you to a particular implementation instead of a particular interface. This commitment can complicate future changes. To avoid it, create objects indirectly.
		Design patterns: [[Abstract Factory]], [[Factory Method]], [[Prototype]]
2. **Dependence on specific operations:** 
	``When you specify a particular operation, you commit to one way of satisfying a request. By avoiding hard-coded requests, you make it easier to change the way a request gets satisfied both at compile-time and at run-time.
		Design patterns: [[Chain of Responsibility]], [[Command]]
3. **Dependence on hardware and software platform:** 
	`External operating system interfaces and application programming interfaces (APIs) are different on different hardware and software platforms. Software that depends on a particular platform will be harder to port to other platforms. It may even be difficult to keep it up to date on its native platform. It's important therefore to design your system to limit its platform dependencies.
		Design patterns: [[Abstract Factory]], [[Bridge]]
﻿﻿﻿4. **Dependence on object representations or implementations:** 
	``Clients that know how an object is represented, stored, located, or implemented might need to be changed when the object changes. Hiding this information from clients keeps changes from cascading. 
		Design patterns: [[Abstract Factory]], [[Bridge]], [[Memento]], [[Proxy]]
﻿﻿5. **Algorithmic dependencies:** 
	﻿﻿``Algorithms are often extended, optimized, and replaced during development and reuse. Objects that depend on an algorithm will have to change when the algorithm changes. Therefore algorithms that are likely to change should be isolated. 
		Design patterns: [[Builder]], [[Iterator]], [[Strategy]], [[Template Method]], [[Visitor]]
﻿﻿﻿6. **Tight coupling:** 
	﻿﻿﻿``Classes that are tightly coupled are hard to reuse in isolation, since they depend on each other. Tight coupling leads to monolithic systems, where you can't change or remove a class without understanding and changing many other classes. The system becomes a dense mass that's hard to learn, port, and maintain. Loose coupling increases the probability that a class can be reused by itself and that a system can be learned, ported, modified, and extended more easily. Design patterns use techniques such as abstract coupling and layering to promote loosely coupled systems.
		Design patterns: [[Abstract Factory]], [[Bridge]], [[Chain of Responsibility]], [[Command]], [[Facade]], [[Mediator]], [[Observer]]
7. **Extending functionality by subclassing:** 
	``Customizing an object by subclassing often isn't easy. Every new class has a fixed implementation overhead (initialization, finalization, etc.). Defining a subclass also requires an in-depth understanding of the parent class. For example, overriding one operation might require overriding another. An overridden operation might be required to call an inherited operation. Subclassing can lead to an explosion of classes, because you might have to introduce many new subclasses for even a simple extension. Object composition in general and delegation in particular provide flexible alternatives to inheritance for combining behavior. New functionality can be added to an application by composing existing objects in new ways rather than by defining new subclasses of existing classes. On the other hand, heavy use of object composition can make designs harder to understand. Many design patterns produce designs in which you can introduce customized functionality just by defining one subclass and composing its instances with existing ones.
		Design patterns: [[Bridge]], [[Chain of Responsibility]], [[Composite]], [[Decorator]], [[Observer]], [[Strategy]]
8. **Inability to alter classes conveniently:** 
	``Sometimes you have to modify a class that can't be modified conveniently. Perhaps you need the source code and don't have it (as may be the case with a commercial class library). Or maybe any change would require modifying lots of existing subclasses. Design patterns offer ways to modify classes in such circumstances.
		Design patterns: [[Adapter]], [[Decorator]], [[Visitor]]

Online Textbook: https://www.cs.unc.edu/~stotts/GOF/hires/contfso.htm