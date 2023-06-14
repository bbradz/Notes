Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Compose objects into trees to represent part-whole hierarchies which can be treated uniformly.

**Motivation**: When Users need to group together components to form larger components which in turn can be used to form even larger components. Composite uses recursive composition. The key is an abstract class that represents *both* primitives and their containers. 

**Use When**
- Wanting to represent part-whole hierarchies of objects.
- Wanting clients to be able to ignore the differences b/w compositions of objects and individual objects.

### Structure

![[Screenshot 2023-06-13 at 1.09.08 PM.png| 500]]

1. Component
		Declares the interface for objects in the composition.
		Implements default behavior or the interface common to all classes, as appropriate.
		Declares an interface for accessing and managing its child components.
		(optional) Defines an interface for accessing a component's parent in the recursive structure, implementing that if doing so is appropriate.
1. Leaf
		Represents leaf objects in the compositions. A leaf has no children.
		Defines behavior for primitive objects in the composition
1. Composite
		Defines behavior for components having children
		Stores child components
		Implements child-related operations in the Component interface.
1. Client
		Manipulates objects in the composition through the Component interface

#### Collaborations
- Clients use the Component class interface to interact with objects in the composite structure. If the recipient is a Leaf, then the request is handled directly. If the recipient is a Composite, then it usually forwards request to its child components, possibly performing additional operations before and/or after forwarding.

### Consequences
- Defines class hierarchies consisting of primitive objects and composite objects. Primitive objects can be composed into more complex objects, which in turn can be composed, and so on recursively. Wherever client code expects a primitive object, it can also take a composite object.
- Makes the client simple. Clients can treat composite structures and individual objects uniformly. Clients normally don't know (and shouldn't care) whether they're dealing with a leaf or a composite component. This simplifies client code, because it avoids having to write tag-and-case-statement-style functions over the classes that define the composition.
- Makes it easier to add new kinds of components. Newly defined Composite or Leaf subclasses work automatically with existing structures and client code. Clients don't have to be changed for new Component classes.
- Can make your design overly general. The disadvantage of making it easy to add new components is that it makes it harder to restrict the components of a composite. Sometimes you want a composite to have only certain components. With Composite, you can't rely on the type system to enforce those constraints for you. You'll have to use run-time checks instead.

### Implementation
1. *Explicit parent references*: Maintaining references from child components to their parent can simplify the traversal and management of a composite structure. The parent reference simplifies moving up the structure and deleting a component. It also helps support [[Chain of Responsibility]] pattern.
2. *Maximizing the Component interface*: One of the goals of the Composite pattern is to make clients unaware of the specific Leaf or Composite classes they're using. To attain this goal, the Component class should define as many common operations for Composite and Leaf classes as possible. The Component class usually provides default implementations for these operations, and Leaf and Composite subclasses will override them.
3. *Declaring the child management operations*: Should we declare operations in the Component and make them meaningful for Leaf classes, or should we declare and define them only in Composite and its subclasses?
4. *Should Component implement a list of Components?* Putting the child pointer in the base class incurs a space penalty for every leaf, even though a leaf never has children. This is worthwhile only if there are relatively few children in the structure.
5. *Child ordering*: When child ordering is an issue, you must design child access and management interfaces carefully to manage the sequence of children. The [[Iterator]] pattern can guide you in this.
7. *Who should delete components?* In languages without garbage collection, it's usually best to make a Composite responsible for deleting its children when it's destroyed. An exception to this rule is when Leaf objects are immutable and thus can be shared.
8. *What's the best data structure for storing components?* Composites may use a variety of data structures to store their children, including linked lists, trees, arrays, and hash tables.

### Related Patterns
Often the component-parent link is used for a [[Chain of Responsibility]]

[[Decorator]] is often used with Composite. When decorators and composites are used together, they will usually have a common parent class. So decorators will have to support the Component interface with operations like Add, Remove, and GetChild

[[Flyweight]] lets you share components, but they can no longer refer to their parents.

[[Iterator]] an be used to traverse composites.

[[Visitor]] localizes operations and behavior that would otherwise be distributed across Composite and Leaf classes