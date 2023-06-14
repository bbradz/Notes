Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
**Also Known As:** Dependents, Publish-Subscribe

**Motivation**: Sometimes many objects are dependent on the information in another object and therefore should be notified of any change in its state.  The Observer pattern describes how to establish these relationships. 

The key objects in this pattern are subject and observer. A subject may have any number of dependent observers. All observers are notified whenever the subject undergoes a change in state. In response, each observer will query the subject to synchronize its state with the subject's state.

**Use When**
- An abstraction has two aspects, one dependent on the other. Encapsulating these aspects in separate objects lets you vary and reuse them independently.
- Change to one object requires changing others, and you don't know how many objects need to be changed.
- An object should be able to notify other objects without making assumptions about who these objects are. You don't want these objects tightly coupled.

### Structure

![[Screenshot 2023-06-14 at 11.28.58 AM.png| 500]]

1. Subject
		Knows its observers. Any number of Observer objects may observe a subject.
		Provides an interface for attaching and detaching Observer objects.
2. Observer
		Defines an updating interface for objects that should be notified of changes in a subject.
3. ConcreteSubject
		Stores state of interest to ConcreteObserver objects.
		Sends a notification to its observers when its state changes.
4. ConcreteObserver
		Maintains a reference to a ConcreteSubject object.
		Stores state that should stay consistent with the subject's.
		Implements the Observer updating interface to keep its state consistent with the subject's

**Collaborations**: 
- ConcreteSubject notifies its observers whenever a change occurs that could make its observers' state inconsistent with its own.
- After being informed of a change in the concrete subject, a ConcreteObserver object may query the subject for information. ConcreteObserver uses this information to reconcile its state with that of the subject.

### Consequences
1. *Abstract coupling b/w Subject and Observer*: All a subject knows is that it has a list of observers, each conforming to the simple interface of the abstract Observer class. The subject doesn't know the concrete class of any observer. Thus the coupling between subjects and observers is abstract and minimal. Because Subject and Observer aren't tightly coupled, they can belong to different layers of abstraction in a system.
2. *Support for broadcast communication*: Freedom to add and remove observers at any time.
3. *Unexpected updates*: A seemingly innocuous operation on the subject may cause a cascade of updates to observers and their dependent objects.

### Implementation
1. *Mapping subjects to their observers*: The simplest way for a subject to keep track of the observers it should notify is to store references to them explicitly in the subject. Alternatively, one can use an associative look-up (a hash table) to maintain the subject-to-observer mapping.
2. *Observing more than one subject*: It might make sense in some situations for an observer to depend on more than one subject. The subject can simply pass itself as a parameter in the Update operation, thereby letting the observer know which subject to examine.
3. *Who triggers the update?* Either: a). Have state-setting operations on Subject call Notify after they change the subject's state, or b). Make clients responsible for calling Notify at the right time.
4. *Dangling references to deleted subjects*: Deleting a subject should not produce dangling references in its observers. One way to avoid dangling references is to make the subject notify its observers as it is deleted so that they can reset their reference to it.
5. *Making sure Subject state is self-consistent before notification*
6. *Avoiding observer-specific update protocols: the push and pull models*: At one extreme, which we call the push model, the subject sends observers detailed information about the change, whether they want it or not. At the other extreme is the pull model; the subject sends nothing but the most minimal notification, and observers ask for details explicitly thereafter.
7. *Specifying modifications of interest explicitly*: You can improve update efficiency by extending the subject's registration interface to allow registering observers only for specific events of interest. When such an event occurs, the subject informs only those observers that have registered interest in that event.
8. *Encapsulating complex update semantics*: When the dependency relationship between subjects and observers is particularly complex, an object that maintains these relationships might be required. We call such an object a **ChangeManager**. Its purpose is to minimize the work required to make observers reflect a change in their subject.

### Related Patterns
[[Mediator]] : By encapsulating complex update semantics, it serves a sort of mediator between subjects and observers.

[[Singleton]] : The ChangeManager may use the Singleton pattern to make it unique and globally accessible.