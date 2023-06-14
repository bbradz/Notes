Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

**Motivation**: Defining an algorithm in terms of abstract operations that subclasses override to provide concrete behavior. Application subclasses define the steps of the algorithm. By defining some of the steps of an algorithm using abstract operations, the template method fixes their ordering, but it lets the subclasses vary those steps to suit their needs.

**Use...**
- to implement the invariant paths of an algorithm once and leave it up to subclasses to implement the behavior that can vary.
- when common behavior among subclasses should be factored and localized in a common class to avoid code duplications.
- to control subclasses extensions. You can define a template method that calls "hook" operations at specific points, thereby permitting extensions only at those points. 

### Structure

![[Screenshot 2023-06-14 at 1.04.57 PM.png| 400]]

1. AbstractClass
		Defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm.
		Implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.
2. ConcreteClass
		Implements the primitive operations to carry out subclass-specific steps of the algorithm.

**Collaborations**: ConcreteClass relies on AbstractClass to implement the invariant steps of the algorithm.

### Consequences
Template methods lead to an inverted control structure that's sometimes referred to as "the Hollywood principle," that is, "Don't call us, we'll call you"

Calls the following kinds of operations:
- concrete operations
- concrete AbstractClass operations that are generally useful to subclasses);
- primitive operations (i.e., abstract operations);
- factory methods
- hook operations which provide default behavior, often nothing, that subclasses can extend if necessary

### Implementation
1. *Minimizing primitive operations* : An important goal in designing template methods is to minimize the number of primitive operations that a subclass must override to flesh out the algorithm.
2. *Naming conventions* : You can identify the operations that should be overridden by adding a prefix to their names.

### Related Patterns
[[Factory Method]]s are often called by template methods.

[[Strategy]] : Template methods use inheritance to vary part of an algorithm. Strategies use delegation to vary the entire algorithm.