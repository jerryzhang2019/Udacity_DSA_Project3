
#Problen_5: Autocomplete with Tries

To generate a suffix, first call "find" on the Trie class to find the prefix. Then, use the returned node. Use recursively to search all nodes in the child node and call yourself until is_word is true.

The time complexity is O(n) , because I have to traverse all the nodes in the tree

The space complexity is O(1), because Because no new variables are created in memory.
