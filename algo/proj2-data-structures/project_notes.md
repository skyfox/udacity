# Show Me the Data Structure

Please see tests in {task}_test.py files. All tests pass. 

## LRU Cache

My implementation of LRU cache relies on 2 data structures:

- Linked list
- Hash map

Python standard library does not provide linked list data structure. Hence I made my own implementation.
I do not expect users to use linked list directly from my library. It is marked as private.

Both get and set LRU cache operations have O(1) time complexity. The cache does lookups in the internal
dict and returns it if it present. Plus promotes the node to the top. Promoting to head takes constant
time because the dict element is a reference to the element in the linked list. In the linked list I 
keep the reference to head. Swapping 2 elements when both are known by their references takes O(1).  

## File Recursion

File recursion task is a classical recursive tree traversal problem with filtering nodes by a specific
condition. Very often it is very easy and straightforward to replace recursion with a queue. It this 
case there is no chance to reach the max recursion depth and the implementation will work even for 
hugh number over folded files and directories. The only limit is a memory for paths and found files. 

The time complexity is O(n) where n is a number of files and directories in a given path. Each files and
directory will be checked exactly once.

## Huffman Coding

Huffman encoding function will build max-heap from the input. It will take 
[linear time](https://docs.python.org/3/library/heapq.html#heapq.heapify). 
O(nlog(n)) will be taken to build prefix tree. Approx linear time will take to build
codes dict because we need to traverse ("walk") the tree. Hence the complexity is O(nlog(n)).

Decoding is simple and does not use, does not build a prefix tree. It has some traits of greedy
algorithms: it maintains 2 pointers and relies on the fact that every prefix in the tree is unique.
It takes O(n) to decode the a given binary representation of the string. Each dict lookup takes a 
constant time.

## Active Directory

Very similar to __File Recursion__, but will stop the execution if the user was found. Hence in worst
case scenario will do O(n) operations where n is the number of groups and users. I also found given
Group class very redundant and simplified it to the way it is easy to read.

## Blockchain

My blockchain implementation is a singly linked list with a pointer to the tail. It also does some 
constant time hashing operations. Adding (append) a block to the chain will take linear time. I also do
not expect users to use _Block class. It is marked as private. Since the tail is a pointer it takes
O(1) to get the last record in the chain and O(n) to get to the head.

## Union and Intersection of Two Linked Lists

The implementation is a classical linked list with additional set field. It does not slow down
insertions, but does increase memory consumption 2 times in worst case when all list values are unique.
However it provides linear time O(n+m) for union, n and m - numbers of elements in the lists 
and similar linear complexity O(min(len(list1), len(list2)) for intersection.    