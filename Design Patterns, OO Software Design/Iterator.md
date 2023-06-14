Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
**Also Known As:** Cursor

**Motivation**: An aggregate object such as a list should give you a way to access its elements without exposing its internal structure. Moreover, you might want to traverse the list in different ways, depending on what you want to accomplish. But you probably don't want to bloat the List interface with operations for different traversals, even if you could anticipate the ones you will need. You might also need to have more than one traversal pending on the same list.

**Use to..**
- Access an aggregate object's contents without exposing its internal representation.
- Support multiple traversals of aggregate objects.
- Provide a uniform interface for traversing different aggregate structure

### Structure

![[Screenshot 2023-06-14 at 10.28.29 AM.png| 500]]

1. Iterator
		Defines an interface for accessing and traversing elements.
2. ConcreteIterator
		Implements the Iterator interface.
		Keeps track of the current position in the traversal of the aggregate.
3. Aggregate
		Defines an interface for creating an Iterator object.
4. ConcreteAggregate
		Implements the Iterator creation interface to return an instance of proper ConcreteIterator

**Collaborations**: A ConcreteIterator keeps track of the current object in the aggregate and can compute the succeeding object in the traversal.

### Consequences
1. _It supports variations in the traversal of an aggregate._ Complex aggregates may be traversed in many ways. For example, code generation and semantic checking involve traversing parse trees. Code generation may traverse the parse tree inorder or preorder. Iterators make it easy to change the traversal algorithm: Just replace the iterator instance with a different one. You can also define Iterator subclasses to support new traversals.
2. _Iterators simplify the Aggregate interface._ Iterator's traversal interface obviates the need for a similar interface in Aggregate, thereby simplifying the aggregate's interface.
3. _More than one traversal can be pending on an aggregate._ An iterator keeps track of its own traversal state. Therefore you can have more than one traversal in progress at once.

### Implementation
1. _Who controls the iteration?_ A fundamental issue is deciding which party controls the iteration, the iterator or the client that uses the iterator. When the client controls the iteration, the iterator is called an **external iterator**, and when the iterator controls it, the iterator is an **internal iterator**
2. _Who defines the traversal algorithm?_ The iterator is not the only place where the traversal algorithm can be defined. The aggregate might define the traversal algorithm and use the iterator to store just the state of the iteration.
3. _How robust is the iterator?_ It can be dangerous to modify an aggregate while you're traversing it. If elements are added or deleted from the aggregate, you might end up accessing an element twice or missing it completely. A simple solution is to copy the aggregate and traverse the copy, but that's too expensive to do in general.
4. _Additional Iterator operations._ The minimal interface to Iterator consists of the operations First, Next, IsDone, and CurrentItem. Some additional operations might prove useful, for example: Previous.

### Related Patterns
[[Composite]] : Iterators are often applied to recursive structures such as Composites.

[[Factory Method]] : Polymorphic iterators rely on factory methods to instantiate the appropriate Iterator subclass.

[[Memento]] : Often used in conjunction w/ the Iterator pattern. Iterator can use memento to capture the state of an iteration. The iterator stores the memento internally.