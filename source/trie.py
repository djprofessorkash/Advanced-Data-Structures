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
        """ Method that adds child as node object in Trie structure. """
        if not isinstance(key, Trie_Node):
            self.children[key] = Trie_Node(key, data)
        else:
            self.children[key.label] = key

    def _get_item(self, key):
        """ Helper method that grabs node's value by key index. """
        return self.children[key]

""" ==================================================
================ TRIE STRUCTURE CLASS ================
================================================== """

class Trie(object):

    def __init__(self):
        """ Class initializer. """
        self.head = Trie_Node()

    def _get_item(self, key):
        """ Helper method that gets data from head of Trie structure. """
        return self.head.children[key]

    def add_word(self):
        """ Method that adds word by adding/traversing letters in Trie structure. """
        pass

    def contains_word(self):
        pass

    def starts_with_prefix(self, prefix):
        pass

    def get_data_by_word(self, word):
        pass