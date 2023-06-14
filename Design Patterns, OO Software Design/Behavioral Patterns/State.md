Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Allow an object to alter its behavior when its internal state changes, appearing to change its class.
**Also Known As:** Objects for States

**Motivation**: The introduction of a common interface to represent all the different possible operational states which need to be interacted with. Each of the states implement state-specific behavior of the abstract State class.

**Use When**
- An object's behavior depends on its state, and it must change its behavior at run-time depending on that state.
- Operations have large, multipart conditional statements that depend on the object's state. This state is usually represented by one or more enumerated constants. Often, several operations will contain this same conditional structure. The State pattern puts each branch of the conditional in a separate class. This lets you treat the object's state as an object in its own right that can vary independently from other objects.

### Structure

![[Screenshot 2023-06-14 at 12.29.52 PM.png| 500]]

1. Context
		Defines the interface of interest to clients.
		Maintains an instance of a ConcreteState subclass that defines the current state.
2. State
		Defines an interface for encapsulating the behavior associated with a particular state of the Context.
3. ConcreteState subclasses
		Each subclass implements a behavior associated with a state of the Context.

**Collaborations**: 
- Context delegates state-specific requests to the current ConcreteState object.
- Context may pass itself as an argument to the State object handling the request. This lets the State object access the context if necessary.
- Context is the primary interface for clients. Clients can configure a context with State objects. Once a context is configured, its clients don't have to deal with the State objects directly. 
- Either Context or the ConcreteState subclasses can decide which state succeeds another and under what circumstances.

### Consequences
1. *It localizes state-specific behavior and partitions behavior for different states*: The State pattern puts all behavior associated with a particular state into one object. Because all state-specific code lives in a State subclass, new states and transitions can be added easily by defining new subclasses.
2. *It makes state transitions explicit*: When an object defines its current state solely in terms of internal data values, its state transitions have no explicit representation; they only show up as assignments to some variables. Introducing separate objects for different states makes the transitions more explicit.
3. *State objects can be shared*: If State objects have no instance variables—that is, the state they represent is encoded entirely in their type—then contexts can share a State object. When states are shared in this way, they are essentially flyweights (see: [[Flyweight]]) with no intrinsic state, only behavior.

### Implementation
1. *Who defines the state transitions?* : The State pattern does not specify which participant defines the criteria for state transitions. If the criteria are fixed, then they can be implemented entirely in the Context. It is generally more flexible and appropriate, however, to let the State subclasses themselves specify their successor state and when to make the transition. This requires adding an interface to the Context that lets State objects set the Context's current state explicitly. Decentralizing the transition logic in this way makes it easy to modify or extend the logic by defining new State subclasses.
2. *A table-based alternative* : Optionally using tables to map inputs to state transitions. For each state, therefore, a table maps every possible input to a succeeding state. This converts conditional code into a table look-up.
3. *Creating and destroying State objects*: Should one create State objects only when they are needed and destroy them thereafter or should they create them ahead of time and never destroy them? The first choice is preferable when the states that will be entered aren't known at run-time, _and_ contexts change state infrequently. This approach avoids creating objects that won't be used, which is important if the State objects store a lot of information. The second approach is better when state changes occur rapidly, in which case you want to avoid destroying states, because they may be needed again shortly. Instantiation costs are paid once up-front, and there are no destruction costs at all. This approach might be inconvenient, though, because the Context must keep references to all states that might be entered.

### Related Patterns
The [[Flyweight]] pattern explains when and how State objects can be shared.

State objects are often [[Singleton]]s.