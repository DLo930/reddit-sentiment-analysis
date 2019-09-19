I've found that most lectures have a pretty well defined "primary
theme" as well as a secondary theme which may be relatively
front-and-center (Big-O is actually most of the lecture on sorting...)
but sometimes the secondary theme is more subtle (underconstrained
specifications). I wanted to document these secondary themes as I
currently understand them.

 - Rob Simmons, June 2015

===== PART ONE
Contracts                Specification vs Implementation
Integers                 Underconstrained Specifications
Arrays                   Safety

Searching                Contract violations vs. contract exploits
Sorting                  Big-O 
Binary Search            Divide and Conquer
Quicksort                Reasoning about recursion
                         Randomness

===== PART TWO
Data Structures          Abstraction: about about lying and deception
Stacks and Queues        Data structure invariants
Linked Lists             Terminating and non-terminating specifications
Unbounded Arrays         Amortized Analysis

Hash Tables              Unpredictability and randomness
Sets                     Equivalence versus equality
Generic Data Strucutres  Object-oriented programming

Binary Search Trees      Structural recursion
AVL Trees                Breaking down a recursive problem into cases

Priority Queues          Worklists
Restoring Invariants     ***

===== PART THREE
Data Structures in C     Memory management
C's Memory Model         Undefined behavior
Types in C               Implementation defined behavior

Virtual Machines         Interpreters versus compilers

Graph Representation     Space versus time tradeoffs
Graph Search             ***
Spanning Trees           Greedy algorithms
Union Find               ***
