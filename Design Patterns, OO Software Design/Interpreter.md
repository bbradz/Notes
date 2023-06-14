Status: #idea
Tags: [[Design Pattern, Reusable OO Software]] [[Behavioral Patterns]]

**Intent**: Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

**Motivation**: If a particular kind of problem occurs often enough, then it might be worthwhile to express instances of the problem as sentences in a simple language. Then you can build an interpreter that solves the problem by interpreting these sentences

**Use When**
There is a possible abstract syntax tree to be constructed..
- The grammar is simple.
- Efficiency is not a critical concern.

### Structure

![[Screenshot 2023-06-14 at 9.52.10 AM.png| 500]]

1. AbstractExpression
		Declares an abstract Interpret operation that is common to all nodes in the abstract syntax tree.
2. TerminalExpression
		Implements an Interpret operation associated with terminal symbols in the grammar.
		An instance is required for every terminal symbol in a sentence.
3. NonterminalExpression
		One such class is required for every rule _R_ ::= R_1 R_2 ... R_n in the grammar.
		Maintains instance variables of type AbstractExpression for each of the symbols R_1 through R_n.
		Implements an Interpret operation for nonterminal symbols in the grammar. Interpret typically calls itself recursively on the variables representing R_1 through R_n.
4. Context
		Contains information that's global to the interpreter.
5. Client
		Builds (or is given) an abstract syntax tree representing a particular sentence in the language that the grammar defines. The abstract syntax tree is assembled from instances of the NonterminalExpression and TerminalExpression classes.
		Invokes the Interpret operation.

**Collaborations**:
- The client builds (or is given) the sentence as an abstract syntax tree of NonterminalExpression and TerminalExpression instances. Then the client initializes the context and invokes the Interpret operation.
- Each NonterminalExpression node defines Interpret in terms of Interpret on each subexpression. The Interpret operation of each TerminalExpression defines the base case in the recursion.
- The Interpret operations at each node use the context to store and access the state of the interpreter.

### Consequences
1. _It's easy to change and extend the grammar._ You can use inheritance to change or extend the grammar. Existing expressions can be modified incrementally, and new expressions can be defined as variations on old ones.
2. _Implementing the grammar is easy, too._ Defining nodes in the abstract syntax tree have similar implementations. These classes are easy to write.
3. _Complex grammars are hard to maintain._ Grammars containing many rules can be hard to manage and maintain. Other design patterns can be applied to mitigate the problem but when the grammar is very complex, other techniques such as parser or compiler generators are more appropriate.
4. _Adding new ways to interpret expressions._ Easier to evaluate an expression by defining a new operation on the expression classes.

### Implementation
1. _Creating the abstract syntax tree._ The abstract syntax tree can be created by a table-driven parser, by a hand-crafted (usually recursive descent) parser, or directly by the client.
2. _Defining the Interpret operation._ You don't have to define the Interpret operation in the expression classes. If common to create a new interpreter, then it's better to use the [[Visitor]] pattern to put Interpret in a separate "visitor" object. For example, a grammar for a programming language will have many operations on abstract syntax trees, such as as type-checking, optimization, code generation, and so on. It will be more likely to use a visitor to avoid defining these operations on every grammar class.
3. _Sharing terminal symbols with the Flyweight pattern._ Grammar whose sentences contain many occurrences of a terminal symbol might benefit from sharing a single copy of that symbol. Grammars for computer programs are good examples—each program variable will appear in many places throughout the code. Terminal nodes generally don't store information about their position in the abstract syntax tree. Parent nodes pass them whatever context they need during interpretation. Hence there is a distinction between shared (intrinsic) state and passed-in (extrinsic) state, and the [[Flyweight]] pattern applies.

### Related Patterns
[[Composite]] : The abstract syntax tree is an instance of the Composite pattern.
[[Flyweight]] : Shows how to share terminal symbols within the abstract syntax tree.
[[Iterator]] : The interpreter can use an Iterator to traverse the structure.
[[Visitor]] : Can be used to maintain the behavior in each node in the abstract syntax tree in one class.