# Trie Node class
class TrieNode:
    def __init__(self):
        # can hold all words of the alphabet
        self.children = [None]*26
        # self.isEndOfWord is set to True if node is the end of a word
        self.isEndOfWord = False
        # most times the trie node has an additional value for each key

# Trie Data Structure class
class Trie:
    # Trie is initialized with a single root node
    def __init__(self):
        self.root = self.get_node()

    # Returns new TrieNode
    def get_node(self):
        return TrieNode()

    # Inserts new key to Trie
    def insert(self, key):
        current = self.root
        for letter in key:
            # get index of of letter
            index = char_to_index(letter)
            # create new TrieNode if there is none at index in current node
            if not current.children[index]:
                current.children[index] = self.get_node()
            # set current node to child node (move down trie)
            current = current.children[index]
        # mark last node as leaf (end of word)
        current.isEndOfWord = True

    # Searches for key in Trie
    def search(self, key):
        current = self.root
        for letter in key:
            # get index of of letter
            index = char_to_index(letter)
            # return false if there is no child at index of node
            if not current.children[index]:
                return False
            # Move down trie
            current = current.children[index]
        # returns whether or not the key is actually in the Trie
        return current.isEndOfWord


def has_children(node):
    # check if a node has children
    for child in node.children:
        if child is not None:
            return True
    return False

# Helper method to get alphabetical index of a char
def char_to_index(char):
    return ord(char) - ord('a')


def delete(root: TrieNode, key: str, depth: int=0):
    pass



# driver code from geeksforgeeks
def main():

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their", "thaw"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
    main()
