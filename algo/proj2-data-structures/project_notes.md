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

Space complexity: It will take at most 2\*capacity\*object_size when the cache is full and all stored
object values are unique.   

## File Recursion

File recursion task is a classical recursive tree traversal problem with filtering nodes by a specific
condition. Very often it is very easy and straightforward to replace recursion with a queue. It this 
case there is no chance to reach the max recursion depth and the implementation will work even for 
hugh number over folded files and directories. The only limit is a memory for paths and found files. 
The tree can be assumed such that the files act as the leaf nodes and the directories act as the
intermediate nodes.

The time complexity is O(n) where n is a number of files and directories in a given path. Each files and
directory will be checked exactly once.

The space complexity: In a worst case, if there is n files in a given directory (flat structure) and 
all of them match a given pattern it will take at most (n-1) list elements. Each element is a 
string of some length. The length of the string can be limited and it is usually limited in
real-world scenario.  

## Huffman Coding

I use Counter which will take a linear time to count the frequency of each char. The n for all
other steps is a length of the counter result. Huffman encoding function will build max-heap from 
this Counter result. 
It will take [linear time](https://docs.python.org/3/library/heapq.html#heapq.heapify). 
O(nlog(n)) will be taken to build prefix tree. Approx linear time will take to build
codes dict because we need to traverse ("walk") the tree. Hence the complexity is O(nlog(n)).

Decoding is simple and does not use, does not build a prefix tree. It has some traits of greedy
algorithms: it maintains 2 pointers and relies on the fact that every prefix in the tree is unique.
It takes O(n) to decode the a given binary representation of the string. Each dict lookup takes a 
constant time.

Space complexity: the biggest memory consumption is in the end of the encoding. The algorithm
needs to store (n\*2-1) nodes and leafs. Each leaf has to hold a string value up to the max number
of unique elements from the input string. Plus codes dict with the length of num_unique_elements.
Decoding takes linear (input size) memory to restore the string based on a given code dict and
does not use additional memory. The interpreter cleans up previous string after the concat
(python strings are immutable).

## Active Directory

Very similar to __File Recursion__, but will stop the execution if the user was found. Hence in worst
case scenario will do O(n) operations where n is the number of groups and users. I also found given
Group class very redundant and simplified it to the way it is easy to read.

Space complexity: is_user_in_group does not hold any intermediate data. It is easy to say there is no memory
consumption outside of a few func variables. But python's stack frame is very expensive -
[almost 500B](https://stackoverflow.com/questions/27564825/recursive-functions-memory-usage).
It is better to avoid deep recursion in python also because of memory limit. Second reason is
a lack tail recursion optimization.

## Blockchain

My blockchain implementation is a singly linked list with a pointer to the tail. It also does some 
constant time hashing operations. Adding (append) a block to the chain will take linear time. I also do
not expect users to use _Block class. It is marked as private. Since the tail is a pointer it takes
O(1) to get the last record in the chain and O(n) to get to the head.

Space complexity: linear. The Blockchain class maintains a pointer to a tail Block. Each block
hold data and a few more fields. Hence the max memory consumption is linear from the input number
of blocks.

## Union and Intersection of Two Linked Lists

The implementation is a classical linked list with additional set field. It does not slow down
insertions, but does increase memory consumption 2 times in worst case when all list values are unique.
The implementation provides linear time O(n+m) for union, n and m - numbers of elements in the lists 
and similar linear complexity O(n+m) for intersection.