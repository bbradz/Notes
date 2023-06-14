Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Encapsulate how objects interact by beeping objects from inter-referring, allowing independent varying interactions.

**Motivation**: OO design encourages distributing behavior among objects which can result in an object structure with many connections between objects; in the worst case, every object ends up knowing about every other Lots of interconnections make it less likely that an object can work without the support of others—the system acts as though it were monolithic. You can avoid these problems by encapsulating collective behavior in a separate mediator object

**Use When**
- Objects communicate in well-defined but complex ways. The resulting interdependencies are unstructured and difficult to understand.
- Reusing an object is difficult b/c it refers to and communicates with many other objects.
- Behavior that's distributed between several classes should be customizable without a lot of subclassing

### Structure

![[Screenshot 2023-06-14 at 11.03.03 AM.png| 500]]

1. Mediator
		Defines an interface for communicating with Colleague objects
2. ConcreteMediator
		Implements cooperative behavior by coordinating Colleague objects.
		Knows and maintains its colleagues.
3. Colleague classes
		Each Colleague class knows its Mediator object.
		Each colleague communicates with its mediator whenever it would have otherwise communicated with another colleague.

**Collaborations**: Colleagues send and receive requests from a Mediator object. The mediator implements the cooperative behavior by routing requests between the appropriate colleague(s).

### Consequences
1. *It limits subclassing*: A mediator localizes behavior that otherwise would be distributed among several objects. Changing this behavior requires subclassing Mediator only; Colleague classes can be reused as is.
2. *It decouples colleagues:* A mediator promotes loose coupling between colleagues. You can vary and reuse Colleague and Mediator classes independently.
3. *It simplifies object protocols*: A mediator replaces many-to-many interactions with one-to-many interactions between the mediator and its colleagues. One-to-many relationships are easier to understand, maintain, and extend.
4. *It abstracts how objects cooperate* Making mediation an independent concept and encapsulating it in an object lets you focus on how objects interact apart from their individual behavior. That can help clarify how objects interact in a system.
5. *It centralizes control*: The Mediator pattern trades complexity of interaction for complexity in the mediator. Because a mediator encapsulates protocols, it can become more complex than any individual colleague. This can make the mediator itself a monolith that's hard to maintain.

### Implementation
1. *Omitting the abstract Mediator class*: There's no need to define an abstract Mediator class when colleagues work with only one mediator. The abstract coupling that the Mediator class provides lets colleagues work with different Mediator subclasses, and vice versa.
2. *Colleague-Mediator communication*: Colleagues have to communicate with their mediator when an event of interest occurs. One approach is to implement the Mediator as an Observer using the [[Observer]] pattern. Colleague classes act as Subjects, sending notifications to the mediator whenever they change state. The mediator responds by propagating the effects of the change to other colleagues.

### Related Patterns
[[Facade]] differs from Mediator in that it abstracts a subsystem of objects to provide a more convenient interface. Its protocol is unidirectional; that is, Facade objects make requests of the subsystem classes but not vice versa. In contrast, Mediator enables cooperative behavior that colleague objects don't or can't provide, and the protocol is multidirectional.

Colleagues can communicate with the mediator using the [[Observer]] pattern.