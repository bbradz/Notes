Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Unified interface for subsystem interfaces. A higher-level interface to make subsystem more usable.

**Motivation**: Structuring a system into subsystems helps reduce complexity. A common design goal is to minimize the communication and dependencies between subsystems. One way to achieve this goal is to introduce a facade object that provides a single, simplified interface to the more general facilities of a subsystem.

**Use When**
- Wanting to provide a simple interface to a complex subsystem. Subsystems get more complex as they evolve. A facade can provide a simple default view of the subsystem that is good enough for most clients.
- Decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
- If you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

### Structure

![[Screenshot 2023-06-13 at 2.27.14 PM.png| 500]]

1. Facade
		Knows which subsystem classes are responsible for a request.
		Delegates client requests to appropriate subsystem objects.
2. subsystem classes
		Implements subsystem functionality.
		Handles work assigned by the Facade object.
		Has no knowledge / keeps no reference to the facade

**Collaborations**: 
- Clients communicate with the subsystem by sending requests to Facade, which forwards them to the appropriate subsystem object(s). Although the subsystem objects perform the actual work, the facade may have to do work of its own to translate its interface to subsystem interfaces.
- Clients that use the facade don't have to access its subsystem objects directly.

### Consequences
1. Shields clients from subsystem components, thus reducing the number of objects that clients deal with and making the subsystem easier to use
2. Promotes weak coupling between the subsystem and its clients. Weak coupling lets you vary the components of the subsystem without affecting its clients. Facades help layer a system and the dependencies between objects. This reduces compilation dependencies which is integral for large software systems.
3. It doesn't prevent applications from using subsystem classes if they need to. Thus you can choose between ease of use and generality.

### Implementation
1. *Reducing client-subsystem coupling*: The coupling b/w clients and the subsystem can be reduced even further by making Facade an abstract class with concrete subclasses for different implementations of a subsystem. This abstract coupling keeps clients from knowing which implementation of a subsystem is used. An alternative to subclassing is to configure a Facade object with different subsystem objects. To customize the facade, simply replace one or more of its subsystem objects.
3. *Public vs. Private subsystem classes*: A subsystem is like a class in that both have interfaces, and both encapsulate something—a class encapsulates state and operations, a subsystem encapsulates classes. And just as it's useful to think of the public and private interface of a class, we can think of the public and private interface of a subsystem. The public interface to a subsystem consists of classes that all clients can access; the private interface is just for subsystem extenders. The Facade class is part of the public interface, of course, but it's not the only part.

### Related Patterns
[[Abstract Factory]] can be used w/ Facade to provide an interface for creating subsystem objects in a subsystem-independent way. Abstract Factory can also be used as an alternative to Facade to hide platform-specific classes.

[[Mediator]] is similar to Facade in that it abstracts functionality of existing classes. However, Mediator's purpose is to abstract arbitrary communication between colleague objects, often centralizing functionality that doesn't belong in any one of them. A mediator's colleagues are aware of and communicate with the mediator instead of communicating with each other directly. In contrast, a facade merely abstracts the interface to subsystem objects to make them easier to use