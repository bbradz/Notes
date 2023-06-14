Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Ensure a class only has one instance, and provide a global point of access to it.

**Motivation**: It's important for some classes to have exactly one instance. A Singleton is a class responsible for keeping track of the sole instance of something. 

**Use When**
- There must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
- When the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code.

### Structure

![[Screenshot 2023-06-12 at 4.07.05 PM.png| 450]]

1. Singleton
		Defines an Instance operation that lets clients access its unique instance. Instance is a class operation.

#### Collaborations
- Clients access a Singleton instance solely through SIngleton's Instance operation

### Consequences
1. *Controlled access to sole instance*: Because the Singleton class encapsulates its sole instance, it can have strict control over how and when clients access it.
2. *Reduced name space*: The Singleton pattern is an improvement over global variables. It avoids polluting the name space with global variables that store sole instances.
3. *Permits refinement of operations and representation*: The Singleton class may be subclassed, and it's easy to configure an application with an instance of this extended class. You can configure the application with an instance of the class you need at run-time.
4. *Permits a variable number of instances*: The pattern makes it easy to change your mind and allow more than one instance of the Singleton class. Moreover, you can use the same approach to control the number of instances that the application uses. Only the operation that grants access to the Singleton instance needs to change.
5. *More flexible than class operations*

### Implementation
1. *Ensuring a unique instance*: The Singleton pattern makes the sole instance a normal instance of a class, but that class must be written so that only one instance can ever be created. A common way to do this is to hide the operation that creates the instance behind a class operation that guarantees only one instance is created. 

### Related Patterns
Many patterns can be implemented using the Singleton pattern. See [[Abstract Factory]], [[Builder]], and [[Prototype]]