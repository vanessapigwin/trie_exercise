class TrieNode:
    def __init__(self, digit='', value=''):
        self.children = [None] * 10 # any node can have children from 0 to 9
        self.operator = []
        self.digit = digit
        self.value = value

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _add_node(self, operator, key, value):
        if key is None or operator is None:
            return False
    
        # iterate through each digit in key
        current = self.root
        for digit in key:
            digit = int(digit)
            if current.children[digit] is None:
                current.children[digit] = TrieNode(digit)

            current = current.children[digit]
        
        # value and operator name is inserted only at the end of key
        if not current.operator:
            current.operator.append(operator)
            current.value = value
        elif current.value > value:
            current.operator = [operator]
            current.value = value
        elif (current.value == value) & (current.operator != [operator]):
            current.operator.append(operator)

    def insert(self, *args):
        for arg in args:
            operator = arg['operator']
            for item in arg['data']:
                key = str(item.split()[0])
                value = float(item.split()[1])
                self._add_node(operator, key, value)
        
    def search(self, key):
        pass

    @staticmethod
    def count_pairs(root):
        result = 0

        if root.operator:
            result += 1

        for digit in root.children:
            if digit is not None:
                result += Trie.count_pairs(digit)
        return result