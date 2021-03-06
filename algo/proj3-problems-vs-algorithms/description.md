# Problems vs. Algorithms

There is no broken or not passing test. Every test for every problem passes.

## 1. Finding the Square Root of an Integer

The algorithm is a modification of binary search.  
Time complexity: O(nlogn). There is just a small difference when the value will be returned in comparison to classical
binary search.  
Space complexity: O(1). There is no non-auxiliary structures to store in the implementation. 

## 2. Search in a Rotated Sorted Array

The algorithm is a modification of binary search. It includes 2 slightly different implementations of binary search.  
Time complexity: O(logn). We run 2 different modification of binary search twice. Each of them has O(logn) time 
complexity. Hence overall algorithm has O(logn) complexity.  
Space complexity: O(1). There is no non-auxiliary structures to store in the implementation.

## 3. Rearrange Array Elements

To sort an input array, I used iterative, queue-based implementation of merge sort. I do not recursively split the
list. Instead I add every element to the queue and "consume" the queue until it has only 1 element. merge() happens
in linear time - (O(n)). I need to merge log(n) times. Hence time complexity of the merge sort is O(nlog(n)).  
On the final merge first and second lists consume O(n) memory. Before the return from merge() function it consumes O(n) 
memory. Hence space complexity is O(n).
Converting str -> int and int -> str takes linear time. However I can assume that all array elements are in the 
range \[0, 9\]. Hence time complexity of finding 2 numbers is O(n) - we need to iterate over sorted array once and
accumulate the result. The same linear time needed to convert str -> int.

Overall time complexity: O(nlog(n)).  
Overall space complexity: O(n).
 
## 4. Dutch National Flag Problem

Typical sorting algorithms (merge sort, quick sort, etc.) rely on the comparison between 2 elements. If a class of
objects implements "equality" and "greater than" (or their opposites) comparison functions, it is sufficient to use 
sorting algorithms with O(nlog(n)) time complexity. In simple words: you don't need to know stones weight to sort them.
You only need to know which one is heavier.  
However, if we deal with a finite and limited class of object, like numbers {0, 1, 2} in this task, we can rely on this
additional information to do sorting faster. This type of sorting is called count sort.   
In a lot of algorithmic applications it useful to check what additional properties input objects and their collections
have. Another well-known example is a presorted array which provides O(log(n)) binary search.

Time complexity: O(n). collections.Counter will take linear time to count 0's, 1's, and 2's. The operation in a loop
will take same linear time.  
Space complexity: O(n). After the loop auxiliary list (sorted_arr) will have the same length as input list. 

## 5. Autocomplete with Tries

Different functions of trie-based autocomplete have different complexity.

Insert time complexity: O(n), where n - is a length of a 'word'.  
Insert memory complexity: O(n). In worst case every word we try to insert consists of unique sequences of chars, for
example 'aaa', 'bbbb', 'cc'. Worst case memory-n is a sum of lengths of inserted words.

Get suffixes time complexity: O(n), where n is a number of nodes in a trie. In worst case a suffix is an empty string.
In this case we need to visit all n nodes of the trie.  
Memory complexity: O(n), where n is all words stored in a trie. In worst case we will return all words built on the way
to nodes with is_word=True attribute.

It might sounds like a slow algorithm, but we see it in action in our mobile devices since forever. The secret is that
the number of words in a language is limited. 300,000-450,000 words for English. People actively use 20,000-50,000.
Actively used words very often have similar prefixes. Hence the time and memory complexity in real-world scenario is
very-very limited and even very low-cost phones can do it very fast.

## 6. Max and Min in a Unsorted Array

Note: I use -∞ and +∞ to compare with. In a case of empty input default (-∞, +∞) will be returned. 

Time complexity: O(n). I iterate over an input array only once.  
Space complexity: O(1). There are only auxiliary elements in the function.


## 7. HTTPRouter using a Trie

Router uses typical implementation of a prefix tree. It has 2 key methods: 

* add_handler
* lookup

Methods does not add a lot of logic on top of trie's methods. Hence the time and space complexity of 
trie's insert/find is the same as router's add_handler/lookup.  
In worst-case scenario the trie will have a form of a linked list. Hence:

time complexity: O(n)  
space complexity: O(n)

where __n__ is a number of unique path components. E.g. for "/path/to/page" there are 3 components: "path", "to", 
and "page". 