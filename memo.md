# Find a cycle in a linked list 
* to find the cycle: Floyd loop detection algorithm (slow, fast pointers, if they meet -> cycle).
* to find the first node in the cycle: let one of the pointers start where the pointers meet, the other at the head of the list. Let them move a step at a time each. They meet at the first node of the cycle.

# DFS / BFS

* DFS (Stack): can be easily implemented with recursion, generally requiries less memory than BFS. Does not find the shortest path to a node while BFS does. 
* BFS (Queue): finds shortest path a starting point and any reachable node, requires more memory.
