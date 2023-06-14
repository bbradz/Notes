Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Use sharing to support large numbers of fine-grained objects efficiently

**Motivation**: Some applications could benefit from using objects throughout their design, but a naive implementation would be prohibitively expensive. The Flyweight pattern describes how to share objects to allow their use at fine granularities without prohibitive cost. A flyweight is a shared object that can be used in multiple contexts simultaneously. The flyweight acts as an independent object in each context—it's indistinguishable from an instance of the object that's not shared.

**Use When *all* of the following are true:***
- An application uses a large number of objects
- Storage costs are high because of the sheer quantity of objects
- Most object state can be made extrinsic
- Many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed
- The application doesn't depend on object identity. Since flyweight objects may be shared, identity tests will return true for conceptually distinct objects.

### Structure

![[Screenshot 2023-06-13 at 8.18.43 PM.png| 500]]

1. Flyweight
		Declares an interface through which flyweights can receive and act on extrinsic state
2. ConcreteFlyweight
		Implements the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable. Any state it stores must be intrinsic; that is, it must be independent of the ConcreteFlyweight object's context.
3. UnsharedConcreteFlyweight
		The Flyweight interface _enables_ sharing; it doesn't enforce it. It's common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure
4. FlyweightFactory
		Creates and manages flyweight objects
		Ensures that flyweights are shared properly. When a client requests a flyweight, the FlyweightFactory object supplies an existing instance or creates one, if none exists.
5. Client
		Maintains a reference to flyweight(s)
		Computes or stores the extrinsic state of flyweight(s)

**Collaborations**: 
- State that a flyweight needs to function must be characterized as either intrinsic or extrinsic. Intrinsic state is stored in the ConcreteFlyweight object; extrinsic state is stored or computed by Client objects. Clients pass this state to the flyweight when they invoke its operations.
- Clients should not instantiate ConcreteFlyweights directly. Clients must obtain ConcreteFlyweight objects exclusively from the FlyweightFactory object to ensure they are shared properly.

### Consequences
Storage savings are a function of several factors:
-   The reduction in the total number of instances that comes from sharing
-   The amount of intrinsic state per object
-   Whether extrinsic state is computed or stored.

The more flyweights are shared, the greater the storage savings. The savings increase with the amount of shared state.

The Flyweight pattern is often combined with the [[Composite]] pattern to represent a hierarchical structure as a graph with shared leaf nodes.

### Implementation
1. *Removing extrinsic state*: Removing extrinsic state won't help reduce storage costs if there are as many different kinds of extrinsic state as there are objects before sharing. Ideally, extrinsic state can be computed from a separate object structure, one with far smaller storage requirements.
2. *Managing shared objects*: Because objects are shared, clients shouldn't instantiate them directly. FlyweightFactory lets clients locate a particular flyweight. FlyweightFactory objects often use an associative store to let clients look up flyweights of interest.

### Related Patterns
The Flyweight pattern is often combined with the [[Composite]] pattern to implement a logically hierarchical structure in terms of a directed-acyclic graph with shared leaf nodes.

It's often best to implement [[State]] and [[Strategy]] objects as flyweights.