Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Add new responsibilities dynamically. An alternative to subclassing for extending functionality.
**Also Known As:** Wrapper

**Motivation**: Adding responsibilities to individual objects, not to an entire class. Instead of inheriting a responsibility meaning that the responsibility has to be there, one can provide an enclosing object which adds on that responsibility as needed.

**Use When**
- Adding responsibilities to individual objects dynamically and transparently, that is, with out affecting other objects
- For responsibilities that can be withdrawn
- When extension by subclassing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination. Or a class definition may be hidden or otherwise unavailable for subclassing.

### Structure

![[Screenshot 2023-06-13 at 2.04.54 PM.png| 500]]

1. Component
		Defines the interface for objects that can have responsibilities added to them dynamically
2. ConcreteComponent
		Defines an object to which additional responsibilities can be attached.
3. Decorator
		Maintains a reference to a Component object and defines an interface that conforms to Component's interface
4. ConcreteDecorator
		Adds responsibilities to the component

**Collaborations**: Decorator forwards requests to its Component object. It may optionally perform additional operations before and after forwarding the request.

### Consequences
Two Benefits:
1. *More flexibility than static inheritance*: Provides a more flexible way to add responsibilities to objects than can be had with static (multiple) inheritance. Responsibilities can be added and removed at run-time simply by attaching and detaching. Furthermore, providing different Decorator classes for a specific Component class lets you mix and match responsibilities.
2. *Avoids feature-laden classes high up in the hierarchy*: Pay-as-you-go approach to adding responsibilities. Instead of trying to support all foreseeable features in a complex, customizable class, you can define a simple class and add functionality incrementally with Decorator objects. Functionality can be composed from simple pieces. As a result, an application needn't pay for features it doesn't use. It's also easy to define new kinds of Decorators independently from the classes of objects they extend.

Two Liabilities:
1. *A decorator and its component aren't identical*: A decorator acts as a transparent enclosure. But from an object identity point of view, a decorated component is not identical to the component itself.
2. *Lots of little objects*: Often results in systems composed of lots of little objects that all look alike. The objects differ only in the way they are interconnected, not in their class or in the value of their variables. Although these systems are easy to customize by those who understand them, they can be hard to learn and debug.

### Implementation
1. *Interface conformance*: A decorator object's interface must conform to the interface of the component it decorates.
2. *Omitting the abstract Decorator class*: There's no need to define an abstract Decorator class when you only need to add one responsibility. That's often the case when you're dealing with an existing class hierarchy rather than designing a new one. In that case, you can merge Decorator's responsibility for forwarding requests to the component into the ConcreteDecorator.
3. *Keeping Component classes lightweight*: To ensure a conforming interface, components and decorators must descend from a common Component class. It's important to keep this common class lightweight; that is, it should focus on defining an interface, not on storing data. The definition of the data representation should be deferred to subclasses; otherwise the complexity of the Component class might make the decorators too heavyweight to use in quantity.
4. *Changing the skin of an object verses changing its guts*: We can think of a decorator as a skin over an object that changes its behavior. An alternative is to change the object's guts. The [[Strategy]] pattern is a good example of a pattern for changing the guts.

### Related Patterns
[[Adapter]] : A decorator is different from an adapter in that a decorator only changes an object's responsibilities, not its interface; an adapter will give an object a completely new interface.

[[Composite]] : A decorator can be viewed as a degenerate composite with only one component. However, a decorator adds additional responsibilities—it isn't intended for object aggregation.

[[Strategy]] : A decorator lets you change the skin of an object; a strategy lets you change the guts. These are two alternative ways of changing an object.