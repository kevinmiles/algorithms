# t9.py

from collections import deque


class DigitTree():

    key_mapping = {
        "a": 2,
        "b": 2,
        "c": 2,
        "d": 3,
        "e": 3,
        "f": 3,
        "g": 4,
        "h": 4,
        "i": 4,
        "j": 5,
        "k": 5,
        "l": 5,
        "m": 6,
        "n": 6,
        "o": 6,
        "p": 7,
        "q": 7,
        "r": 7,
        "s": 7,
        "t": 8,
        "u": 8,
        "v": 8,
        "w": 9,
        "x": 9,
        "y": 9,
        "z": 9,
    }

    class DigitTreeNode():
        def __init__(self):
            self.words = []
            self.children = {}

    def __init__(self):
        self.root = self.DigitTreeNode()

    def digits(self, word):
        return ''.join([str(key_mapping[c]) for c in word])

    def insert(self, word):
        node = self.root
        for digit in self.digits(word):
            if digit not in node.children:
                node.children[digit] = self.DigitTreeNode()
            node = node.children[digit]
        node.words.append(word)

    def search(self, digits):
        node = self.root
        for digit in digits:
            try:
                node = node.children[digit]
            except KeyError:
                return []
        result = []
        agenda = deque([node])
        while len(agenda) > 0:
            node = agenda.popleft()
            result.extend(node.words)
            agenda.extend(node.children.values())
        return result


tree = DigitTree()
words = [
    "roach",
    "roaches",
    "poach",
    "poachers",
    "reach",
    "hello",
    "world"
]
for word in words:
    tree.insert(word)
print tree.search("76224")
print tree.search("73")
