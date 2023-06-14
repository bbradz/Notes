Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Convert Interface of a class into another interface. Lets classes work together that couldn't otherwise.
**Also Known As:** Wrapper

**Motivation**: Allowing a class you want to reuse but which doesn't match the interface your applying it to slot in. The adapter is often responsible for the functionality that the adapted class doesn't provide. 

**Use When**
- To use an existing class, and its interface does not match the one you need
- To create a reusable class that cooperates with unrelated or unforeseen classes without compatible interfaces
- To adapt the interface of parent class for connection to several subclasses which are impractical to adapt each individually

### Structure

![[Screenshot 2023-06-13 at 12.25.05 PM.png| 500]]

1. Target
		Defines the domain-specific interface that Client uses
2. Client
		Collaborates with objects conforming to the Target interface.
3. Adaptee
		Defines an existing interface that needs adapting
4. Adapter
		Adapts the interface of Adaptee to the Target interface

#### Collaborations
- Client call operations on an Adapter instance. In turn, the Adapter calls Adaptee operations that carry out the request

### Consequences
Class Adapter:
- Adapts Adaptee to Target by committing to a concrete Adapter class. As a consequence, a class adapter won't work when we want to adapt a class *and* all its subclasses
- Lets Adapter override some of Adaptee's behavior, since Adapter is a subclass of Adaptee
- Introduces only one object, and no additional pointer indirection is needed to get to the Adaptee

Object Adapter:
- A single Adapter works with many Adaptees, the Adaptee itself and all of its subclasses (if any). Adapter can also add functionality.
- Harder to override Adaptee behavior. It would require subclassing Adaptee and making Adapter refer to the subclass rather than the Adaptee itself.

Other issues:
1. *How much adapting does Adapter do?* Adapters vary in the amount of work they do to adapt Adaptee to the Target interface. There is a spectrum of possible work, from simple interface conversion—for example, changing the names of operations—to supporting an entirely different set of operations. The amount of work Adapter does depends on how similar the Target interface is to Adaptee's.
2. *Pluggable Adapters*: A class is more reusable when you minimize the assumptions other classes must make to use it. By building interface adaptation into a class, you eliminate the assumption that other classes see the same interface. Put another way, interface adaptation lets us incorporate our class into existing systems that might expect different interfaces to the class.
3. *Using two-way adapters to provide transparency*: A potential problem with adapters is that they aren't transparent to all clients. An adapted object no longer conforms to the Adaptee interface, so it can't be used as is wherever an Adaptee object can. **Two-way adapters** can provide such transparency.

### Related Patterns
[[Bridge]] has a structure similar to an object adapter, but Bridge has a different intent: It is meant to separate an interface from its implementation so that they can be varied easily and independently. An adapter is meant to change the interface of an *existing* object.

[[Decorator]] enhances another object without changing its interface. A decorator is thus more transparent to the application than an adapter is. As a consequence, Decorator supports recursive composition, which isn't possible with pure adapters.

[[Proxy]] defines a representative or surrogate for another object and does not change its interface.