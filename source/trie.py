#!python3

""" ==================================================
================== TRIE NODE CLASS ===================
================================================== """

class Trie_Node(object):

    def __init__(self, label=None, data=None):
        """ Class initializer. """
        self.label = label
        self.data = data
        self.children = dict()          # Saves children object as dictionary accessible under current node

    def add_child(self, key, data=None):
        """ 
        Method that adds child as node object in Trie structure.\n
        PARAMS: { key }     ->  char(), str()\t
                { data }    ->  char(), str(), NoneType() (default)\t
        RETURN: { None }    ->  NoneType()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        if not isinstance(key, Trie_Node):
            self.children[key] = Trie_Node(key, data)
        else:
            self.children[key.label] = key

    def _get_item(self, key):
        """ 
        Helper method that grabs node's value by key index.\n
        PARAMS: { key }                 ->  char(), str()\t
        RETURN: { self.children[key] }  ->  char(), str()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        return self.children[key]

""" ==================================================
================ TRIE STRUCTURE CLASS ================
================================================== """

class Trie(object):

    def __init__(self):
        """ Class initializer. """
        self.head = Trie_Node()

    def _get_item(self, key):
        """ 
        Helper method that gets data from head of Trie structure.\n
        PARAMS: { key }                     ->  char(), str()\t
        RETURN: { self.head.children[key] } ->  char(), str()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        return self.head.children[key]

    def add_word(self, word):
        """ 
        Method that adds word by adding/traversing letters in Trie structure.\n
        PARAMS: { word }    ->  char(), str()\t
        RETURN: { None }    ->  char(), str()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        is_word_complete, current_node = True, self.head

        for iterator in range(len(word)):
            if word[iterator] in current_node.children:
                current_node = current_node.children[word[iterator]]
            else:
                is_word_complete = False
                break

        if not is_word_complete:
            while iterator < len(word):
                current_node.add_child(word[iterator])
                current_node = current_node.children[word[iterator]]
                iterator += 1
        
        # NOTE: Stores full word as data at end of word in Trie for testing purposes
        current_node.data = word

    def contains_word(self, word):
        """ 
        Method that checks if input word is contained as depth-first word in Trie structure.\n
        PARAMS: { word }        ->  char(), str()\t
        RETURN: { does_exist }  ->  bool()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        if len(word) < 1:
            return False
        if word is None:
            raise ValueError("Trie.contains_word() requires a non-empty string.")

        current_node, does_exist = self.head, True

        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                does_exist = False
                break

        if does_exist:
            if current_node.data == None:
                does_exist = False

        return does_exist

    def starts_with_prefix(self, prefix):
        """ 
        Method that checks which words contained in Trie structure start with input prefix.\n
        PARAMS: { prefix }          ->  char(), str()\t
        RETURN: { prefixed_words }  ->  list()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        prefixed_words = list()

        if prefix is None:
            raise ValueError("Prefix must not be null/None.")

        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                return prefixed_words
        
        if top_node == self.head:
            prefixes_queue = [node for key, node in top_node.children.items()]
        else:
            prefixes_queue = [top_node]

        while prefixes_queue:
            current_node = prefixes_queue.pop()
            if current_node.data is not None:
                prefixed_words.append(current_node.data)
            prefixes_queue = [node for key, node in current_node.children.items()] + prefixes_queue

        return prefixed_words


    def get_data_by_word(self, word):
        """ 
        Method that grabs and returns data contained by final node in word.\n
        PARAMS: { prefix }          ->  char(), str()\t
        RETURN: { prefixed_words }  ->  list()\n
        RUNTIME (BEST):     O(?)    ->  ???\t
        RUNTIME (WORST):    O(?)    ->  ???\t
        MEMORY (OPTIMAL):   O(?)    ->  ???
        """
        if not self.contains_word(word):
            raise ValueError("{} not found in Trie.".format(word))

        current_node = self.head
        for letter in word:
            current_node = current_node[letter]

        return current_node.data

if __name__ == "__main__":
    trie = Trie()
    words = "hello goodbye help gerald gold tea ted team to too tom stan standard money"

    for word in words.split():
        trie.add_word(word)

    print("'Goodbye' in Trie: {}".format(trie.contains_word("Goodbye")))