
# coding: utf-8

# In[2]:


#Problen5 Autocomplete with Tries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self, prefix = ""):
        generated = self._generate_suffixes(prefix)
        return ",".join(generated)
    
    def _generate_suffixes(self, prefix):
        if self.is_word:
            yield prefix
        for char, node in self.children.items():
            yield from node._generate_suffixes(prefix + char)
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        
    def find(self, prefix):
        node =self.root
        
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

MyTrie = Trie()
for word in wordList:
    MyTrie.insert(word)
    
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');    

#Test cases    
print(MyTrie.find("ant").suffixes())
print(MyTrie.find("f").suffixes())
print(MyTrie.find("t").suffixes())
print(MyTrie.find("trig").suffixes())

