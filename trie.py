#Creates a TrieNode class to represent each node in the Trie
class TrieNode:
    def __init__(self):
        #Initializes a dictionary to store the children of the node
        self.children = {}
        #Initializes a boolean to keep track of whether the node is the end of a word
        self.endOfWord = False
#Create Trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()


    #Create method to add words to Trie
    def add_word(self, word: str) -> None:
        #Start at the root node
        curr_node = self.root
        
        #Iterate through each letter in the word
        for letter in word:
            #If the letter is not in the current node's children, create a new node for the letter
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
                #Move to the node for the next letter
            curr_node = curr_node.children[letter]
        #Set the endOfWord boolean to True for the last letter in the word
        curr_node.endOfWord = True

    #Create method to check if a word is in the Trie
    def check_for_word(self, word: str) -> bool:
        #Start at the root node
        curr_node = self.root

        #Iterate through each letter in the word
        for letter in word:
            #If the letter is not in the current node's children, return False as word does not exist
            if letter not in curr_node.children:
                return False
            #Move to the node for the next letter
            curr_node = curr_node.children[letter]
        #Return True if the last letter in the word is the end of a word
        return curr_node.endOfWord
        
    #Create method to check for a substring
    def substring_check(self, substring: str) -> list:
        words = []

        #Create a helper function to search for words in the Trie
        def search_words(node, current_word):
            #If the node is the end of a word, add the current word to the list of words
            if node.endOfWord:
                if current_word not in words:
                    words.append(current_word)
        #Helper function to find all substrings of the given substring
        def find_substrings(node, current_substring):
            for letter in node.children:
                new_substring = current_substring + letter
                #Search for words in the Trie that contain the substring
                search_words(node.children[letter], new_substring)
                #Recursively find substrings
                find_substrings(node.children[letter], new_substring)

        def is_valid_substring_word(word):
            # Check if the word contains the given substring and not its separate or reversed form.
            return substring in word and word != substring and word[::-1] != substring

        
        find_substrings(self.root, "")
        # Filter words to only include valid words with the given substring.
        valid_words = [word for word in words if is_valid_substring_word(word)]
        return valid_words


    #Create method to print all words in the Trie
    def print_words(self):
        #Create a helper function to search for words in the Trie
        def search_words(node, current_word):
            if node.endOfWord:
                words.append(current_word)

            for letter, child_node in node.children.items():
                search_words(child_node, current_word + letter)

        words = []
        #Call helper function to search for words in the Trie with an empty current word
        search_words(self.root, "")
        
        #Print all words in the Trie if they exist
        if words:
            print("The current words in the Trie are:")
            for word in words:
                print(word)
        else:
            #Print message if the Trie is empty
            print("The Trie is currently empty.")