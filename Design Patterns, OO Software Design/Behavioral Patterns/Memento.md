Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Capture and externalize an object's internal state so it can be restored to this state later.
**Also Known As:** Token

**Motivation**: Recording the internal state of an object. This is required when implementing checkpoints and undo mechanisms that let users back out of tentative operations or recover from errors.

**Use When**
- A snapshot of (some portion of) an object's state must be saved so that it can be restored to that state later, *and*
- A direct interface to obtaining the state would expose implementation details and break the object's encapsulation

### Structure

![[Screenshot 2023-06-14 at 11.11.37 AM.png| 500]]

1. Memento
		Stores internal state of the Originator object. May store as much or as little of the originator's internal state as necessary at it's originator's discretion.
		Protects against access by objects other than the originator. Mementos have effectively two interfaces. Caretaker sees a _narrow_ interface to the Memento—it can only pass the memento to other objects. Originator, in contrast, sees a _wide_ interface, one that lets it access all the data necessary to restore itself to its previous state. Ideally, only the originator that produced the memento would be permitted to access the memento's internal state.
2. Originator
		Creates a memento containing a snapshot of its current internal state.
		Uses the memento to restore its internal state.
3. Caretake
		Is responsible for the memento's safekeeping.
		Never operates on or examines the contents of a memento.

**Collaborations**: 
- A caretaker requests a memento from an originator, holds it for a time, and passes it back to the originator.
- Mementos are passive. Only the originator that created a memento will assign or retrieve its state.

### Consequences
1. *Preserving encapsulation boundaries*: Memento avoids exposing information that only an originator should manage but that must be stored nevertheless outside the originator. The pattern shields other objects from potentially complex Originator internals, thereby preserving encapsulation boundaries.
2. *Using mementos might be expensive*: Mementos might incur considerable overhead if Originator must copy large amounts of information to store in the memento or if clients create and return mementos to the originator often enough.
3. *Defining narrow and wide interfaces*: It may be difficult in some languages to ensure that only the originator can access the memento's state.
4. *Hidden costs in caring for mementos*: A caretaker is responsible for deleting the mementos it cares for. However, the caretaker has no idea how much state is in the memento. Hence an otherwise lightweight caretaker might incur large storage costs when it stores mementos.

### Implementation
1. *Language support*: Mementos have two interfaces: a wide one for originators and a narrow one for other objects. Ideally the implementation language will support two levels of static protection.
2. *Storing incremental changes*: When mementos get created and passed back to their originator in a predictable sequence, then Memento can save just the _incremental change_ to the originator's internal state.

### Related Patterns
[[Command]] : Commands can use mementos to maintain state for undoable operations.

[[Iterator]] : Mementos can be used for iteration as described earlier.