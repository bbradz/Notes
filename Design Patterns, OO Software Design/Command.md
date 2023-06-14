Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
**Also Known As:** Action, Transaction

**Motivation**: The Command pattern lets toolkit objects make requests of unspecified application objects by turning the request itself into an object. This object can be stored and passed around like other objects. The key to this pattern is an abstract Command class, which declares an interface for executing operations. In the simplest form this interface includes an abstract Execute operation. Concrete Command subclasses specify a receiver-action pair by storing the receiver as an instance variable and by implementing Execute to invoke the request.

**Use When**
- You feel the need to parameterize objects by an action to perform.
- Needing to specify, queue, and execute requests at different times. A Command object can have a lifetime independent of the original request.
- Wanting to support undo. The Command's Execute operation can store state for reversing its effects in the command itself.
- Needing to log changes so that they can be reapplied in case of a system crash.
- Structuring a system around high-level operations built on primitives operations.

### Structure

![[Screenshot 2023-06-14 at 9.40.37 AM.png| 500]]

1. Command
		Declares an interface for executing an operation.
2. ConcreteCommand
		Defines a binding between a Receiver object and an action.
		Implements Execute by invoking the corresponding operation(s) on Receiver.
3. Client
		Creates a ConcreteCommand object and sets its receiver.
4. Invoker
		Asks the command to carry out the request.
5. Receiver
		Knows how to perform the operations associated with carrying out a request. Any class may serve as a Receiver.

**Collaborations**: 
- The client creates a ConcreteCommand object and specifies its receiver.
- An Invoker object stores the ConcreteCommand object.
- The invoker issues a request by calling Execute on the command. When command need to be undoable, ConcreteCommand stores state for undoing the command prior to invoking Execute.
- The ConcreteCommand object invokes operations on its receiver to carry out the request.

### Consequences
1. Command decouples the object that invokes the operation from the one that knows how to perform it.
2. Commands are first-class objects. They can be manipulated and extended like any other object.
3. You can assemble commands into a composite command. An example is the MacroCommand class described earlier. In general, composite commands are an instance of the [[Composite]] pattern.
4. It's easy to add new Commands, because you don't have to change existing classes.

### Implementation
1. _How intelligent should a command be?_ A command can have a wide range of abilities. At one extreme it merely defines a binding between a receiver and the actions that carry out the request. At the other extreme it implements everything itself without delegating to a receiver at all. The latter extreme is useful when you want to define commands that are independent of existing classes, when no suitable receiver exists, or when a command knows its receiver implicitly.
2. _Supporting undo and redo._ To support one level of undo, an application needs to store only the command that was executed last. For multiple-level undo and redo, the application needs a **history list** of commands that have been executed, where the maximum length of the list determines the number of undo/redo levels. The history list stores sequences of commands that have been executed. Traversing backward through the list and reverse-executing commands cancels their effect; traversing forward and executing commands reexecutes them.
3. _Avoiding error accumulation in the undo process._ Hysteresis can be a problem in ensuring a reliable, semantics-preserving undo/redo mechanism. Errors can accumulate as commands are executed, unexecuted, and reexecuted repeatedly so that an application's state eventually diverges from original values. It may be necessary therefore to store more information in the command to ensure that objects are restored to their original state.

### Related Patterns
A [[Composite]] can be used to implement MacroCommands.
A [[Memento]] can keep the state the command requires to undo its effect.
A command that must be copied before being placed on the history list acts as a [[Prototype]]