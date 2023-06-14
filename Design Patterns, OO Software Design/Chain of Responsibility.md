Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

**Motivation**: Sometimes it's natural to organize help information according to its generality—from the most specific to the most general. Furthermore, it's clear that a help request is handled by one of several user interface objects; which one depends on the context and how specific the available help is. This pattern is to decouple senders and receivers by giving multiple objects a chance to handle a request. The request gets passed along a chain of objects until one of them handles it.

**Use When**
- More than one object may handle a request, and the handler isn't known _a priori_. The handler should be ascertained automatically.
- You want to issue a request to one of several objects without specifying the receiver explicitly.
- The set of objects that can handle a request should be specified dynamically.

### Structure

![[Screenshot 2023-06-14 at 9.06.24 AM.png| 500]]

1. Handler
		Defines an interface for handling requests.
		(optional) Implements the successor link.
2. ConcreteHandler
		Handles requests it is responsible for.
		Can access its successor.
		If the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor.
3. Client
		Initiates the request to a ConcreteHandler object on the chain.

**Collaborations**: When a client issues a request, the request propagates along the chain until a ConcreteHandler object takes responsibility for handling it.

### Consequences
1. *Reduced coupling*: This frees an object from knowing which other object handles a request. An object only has to know that a request will be handled "appropriately". An object in the chain doesn't have to know about the chain's structure, simplifying interconnections.
2. *Added flexibility in assigning responsibilities to objects*: Added flexibility in distributing responsibilities among objects. You can add or change responsibilities for handling a request by adding to or otherwise changing the chain at run-time.
3. *Receipt isn't guaranteed*: Since a request has no explicit receiver, there's no guarantee it'll be handled.

### Implementation
1. *Implementing the successor chain*: Implement the successor chain using existing links works well when the links support the chain you need. It saves you from defining links explicitly, and it saves space. But if the structure doesn't reflect the chain of responsibility your application requires, then you'll have to define redundant links.
2. *Connecting successors*: If there are no preexisting references for defining a chain, then you'll have to introduce them yourself. In that case, the Handler not only defines the interface for the requests but usually maintains the successor as well. That lets the handler provide a default implementation of HandleRequest that forwards the request to the successor (if any). If a ConcreteHandler subclass isn't interested in the request, it doesn't have to override the forwarding operation, since its default implementation forwards unconditionally.
3. *Representing requests*: In the simplest form, the request is a hard-coded operation invocation. An alternative is to use a single handler function that takes a request code as a parameter. 

### Related Patterns
Chain of Responsibility is often applied in conjunction with [[Composite]]. There, a component's parent can act as its successor.