Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

**Motivation**: Copying or "cloning" an instance of a inaccessible subclass. 

**Use When**
A system should be independent of how its products are created, composed, and represented; *and*
- When the classes to instantiate are specified at run-time, for example, by dynamic loading; *or*
- To avoid building a class hierarchy of factories that parallels the class hierarchy of products; *or*
- When instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state.

### Structure

![[Screenshot 2023-06-12 at 3.23.09 PM.png| 500]]

1. Prototype
		Declares an interface for cloning itself.
2. ConcretePrototype
		Implements an operation for cloning itself.
3. Client
		Creates a new object by asking a prototype to clone itself

#### Collaborations
- A client asks a prototype to clone itself

### Consequences
Prototype has many of the same consequences that [[Abstract Factory]] and [[Builder]] have: It hides the concrete product classes from the client, thereby reducing the number of names clients know about Moreover, these patterns let a client work with application-specific classes without modification. 

Additional benefits of the Prototype pattern are:
1. *Adding and removing products at run-time*: Prototypes let you incorporate a new concrete product class into a system simply by registering a prototypical instance with the client. That's a bit more flexible than other creational patterns, because a client can install and remove prototypes at run-time.
2. *Specifying new objects by varying values*: Highly dynamic systems let you define new behavior through object composition-- by specifying values for an object's variables, for example-- and not by defining new classes. You effectively define new kinds of objects by instantiating existing classes and registering the instances as prototypes of client objects. A client can exhibit new behavior by delegating responsibility to the prototype. This allows users to define new "classes" w/o programming.
3. *Specifying new objects by varying structure*: Many applications build objects from parts and subparts. Editors for circuit design, for example, build circuits out of subcircuits. The Prototype pattern supports this as well by simply adding this subcircuit as a prototype to the palette of available circuit elements.
4. *Reduced subclassing*: [[Factory Method]] often produces a hierarchy of Creator classes that parallels the product class hierarchy. The Prototype pattern lets you clone a prototype instead of asking a factory method to make a new object. Hence eliminating any Creator class hierarchy at all.

The main liability of the Prototype pattern is that each subclass of Prototype must implement the *Clone()* operation, which may be difficult. 

### Implementation
Consider the following issues when implementing prototypes:
1. *Using a prototype manager*: When the number of prototypes in a system isn't fixed (that is, they can be created an destroyed dynamically), keep a registry of available prototypes. Clients won't manage prototypes themselves but will store and retrieve them from the registry. A client will ask the registry for a prototype before cloning it. This is a prototype manager.
2. *Implementing the Clone operation*: The hardest part of the Prototype pattern, especially when object structures contain circular references. 
3. *Initializing clones:* While some clients are perfectly happy with the clone as is, others will want to initialize some or all of tis internal state to values of their choosing. You generally can't pass these values in the Clone operation, because their number will vary between classes of prototypes. Some prototypes might need multiple initialization parameters; other won't need any. Passing parameters in the Clone operation precludes a uniform cloning interface. 

### Related Patterns
Prototype and [[Abstract Factory]] are competing patterns in some ways. They can also be used together though. An Abstract Factory might store a set of prototypes from which to clone and return product objects.

Designs that make heavy use of the [[Composite]] and [[Decorator]] patterns often can benefit from Prototype as well.