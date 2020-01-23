# Problems vs. Algorithms

There is no broken or not passing test. Every test for every problem passes.

## Dutch National Flag Problem

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

## Max and Min in a Unsorted Array

Note: I use -∞ and +∞ to compare with. In a case of empty input default (-∞, +∞) will be returned. 

Time complexity: O(n). I iterate over an input array only once.  
Space complexity: O(1). There are only auxiliary elements in the function.