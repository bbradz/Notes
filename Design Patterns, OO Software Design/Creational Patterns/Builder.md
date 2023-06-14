Status: #idea
Tags: [[Design Pattern, Reusable OO Software]]

**Intent**: Separate construction from its representation so that the process can create different representations.

**Motivation**: Take the mechanism for creating and assembling a complex object step-by-step and put it behind an abstract interface. A director outsources to it's builder classes the separated algorithm for assembling objects.

**Use When**
- The algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
- The construction process must allow different representations for the object that's constructed

### Structure

![[Screenshot 2023-06-12 at 2.06.01 PM.png| 500]]

1. Builder
		Specifies an abstract interface for creating parts of a Product object
2. ConcreteBuilder
		Constructs and assembles parts of the product by implementing the Builder interface
		Defines and keeps track of the representation it creates
		Provides an interface for retrieving the product
3. Director
		Constructs an object using the Builder interface
4. Product
		Represents the complex object under construction. ConcreteBuilder builds the product's internal representation and defines the process by which it's assembled. 
		Includes classes that define the constituent parts, including interfaces for assembling the parts into the final result

#### Collaborations
- The client creates the Director object and configures it with the desired Builder object
- Director notifies the builder whenever a part of the product should be built
- Builder handles requests from the director and adds parts to the product
- The client retrieves the product from the builder

### Consequences
1. *It lets you vary a product's internal representation*: The Builder object provides the director with an abstract interface for constructing the product. The interface lets the builder hide the representation and internal structure of the product. It also hides how the product gets assembled. Because the product is constructed through an abstract interface, all you have to do to change the product's internal representation is define a new kind of builder.
2. *It isolates code for construction and representation*: The Builder pattern improves modularity by encapsulating the way a complex object is constructed and represented. Clients needn't know anything about the classes that define the product's internal structure; such classes don't appear in Builder's interface.
3. *It gives you finer control over the construction process*: Unlike creational patterns that construct products in one shot, the Builder pattern constructs the product step by step under the director's control. Only when the product is finished does the director retrieve it from the builder. Hence the Builder interface reflects the process of constructing the product more than other creational patterns. This gives you finer control over the construction process and consequently the internal structure of the resulting product.

### Implementation
Typically an abstract Builder class defines an operation for each component that a director asks it to create. The operations do nothing by default. A ConcreteBuilder class overrides operations for components it's interested in creating.

Issues to consider include:
1. *Assembly and construction interface*: Builders construct their products in step-by-step fashion. Therefore the Builder class interface must be general enough to allow the construction of products for all kinds of concrete builders. A key design issue concerns the model for the construction and assembly process. A model where the results of construction requests are simply appended to the product is usually sufficient. But sometimes you might need access to parts of the product constructed earlier.
2. *Why no abstract class for products?* In the common case, the products produced by concrete builders differ so much in representation that there's little benefit giving different products a common parent class.
3. *Empty methods as default in Builder

### Related Patterns
[[Abstract Factory]] is similar to Builder in that it also constructs complex objects. The primary difference is that the Builder pattern focuses on constructing a complex object step-by-step. Abstract Factory's emphasis is on families of product objects. Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.

A [[Composite]] is what the builder often builds.