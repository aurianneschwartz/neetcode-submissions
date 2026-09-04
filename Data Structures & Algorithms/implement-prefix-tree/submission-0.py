class Node:
    
    def __init__(self,letter):
        self.letter = letter
        self.next = {}
        self.final = False

    def getChild(self, letter) -> Node :
        if letter not in self.next:
            return None
        return self.next[letter]
    
    def addChild(self, letter):
        if letter in self.next:
            return self.next[letter]
        self.next[letter] = Node(letter)
        return self.next[letter]

    
    def makeFinal(self):
        self.final = True

class PrefixTree:

    def __init__(self):
        self.root  = Node('')


    def insert(self, word: str) -> None:
        current_node = self.root
        for i, letter in enumerate(word):
            current_node = current_node.addChild(letter)
            if i == len(word)-1:
                current_node.makeFinal()


    def search(self, word: str) -> bool:
        current_node = self.root
        for i, letter in enumerate(word):
            current_node = current_node.getChild(letter)
            if current_node == None:
                return False
        if current_node.final:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for i, letter in enumerate(prefix):
            current_node = current_node.getChild(letter)
            if current_node == None:
                return False
        return True
        