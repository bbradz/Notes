Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Provide a surrogate or placeholder for another object to control access to it.
**Also Known As:** Surrogate

**Motivation**: Using another object, a proxy, that acts as a stand-in for the real object. The proxy acts just like the object and takes care of instantiating it when it's required. Controlling access to an object defers the full cost of its creation and initialization until we actually need to use it.

**Use When**
- Remote proxy: provides a local representative for an object in a different address space.
- Virtual proxy: creates expensive objects on demand. 
- Protection proxy: controls access to the original object, useful when objects should have different access rights.
- Smart reference: a replacement for a bare pointer that performs additional actions when an object is accessed. Typical uses include:
	- Counting the number of references to the real object so that it can be freed automatically when there are no more references
	- Loading a persistent object into memory when it's first referenced
	- Checking that the real object is locked before it's accessed to ensure that no other object can change it

### Structure

![[Screenshot 2023-06-13 at 8.48.05 PM.png| 500]]

1. Proxy
		Maintains a reference that lets the proxy access the real subject. Proxy may refer to a Subject if the RealSubject and Subject interfaces are the same.
		Provides an interface identical to Subject's so that a proxy can be substituted for the real subject.
		Controls access to the real subject and may be responsible for creating and deleting it.
		Other responsibilities depend on the kind of proxy:
			- *remote proxies* : are responsible for encoding a request and its arguments and for sending the encoded request to the real subject in a different address space.
			- *virtual proxies* : may cache additional information about the real subject so that they can postpone accessing it. For example, the ImageProxy from the Motivation caches the real image's extent.
			- *protection proxies* : check that the caller has the access permissions required to perform a request.
2. Subject
		Defines the common interface for RealSubject and Proxy so that a Proxy can be used anywhere a RealSubject is expected.
3. RealSubject
		Defines the real object that the proxy represents

**Collaborations**: Proxy forwards requests to RealSubject when appropriate, depending on the kind of proxy.

### Consequences
The Proxy pattern introduces a level of indirection when accessing an object. The additional indirection has many uses, depending on the kind of proxy:
1. A remote proxy can hide the fact that an object resides in a different address space.
2. A virtual proxy can perform optimizations such as creating an object on demand.
3. Both protection proxies and smart references allow additional housekeeping tasks when an object is accessed.

Additionally, Copy-on-write can reduce the cost of copying heavyweight subjects significantly.

### Related Patterns
[[Adapter]] : An adapter provides a different interface to the object it adapts. In contract, a proxy provides the same interface as its subject. However, a proxy used for access protection might refuse to perform an operation that the subject will perform, so its interface may be effectively a subset of the subject's.

[[Decorator]] : Although decorators can have similar implementations as proxies, decorators have a different purpose. A decorator adds one or more responsibilities to an object, whereas a proxy controls access to an object.

Proxies vary in the degree to which they are implemented like a decorator.