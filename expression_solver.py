# expression_solver.py

import os, sys

parens = set(['(' ,')'])
operators = set(['+','-','*','/'])
digits = set(['0','1','2','3','4','5','6','7','8','9'])

def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in parens or expression[i] in operators:
            tokens.append(expression[i])
            i += 1
        elif expression[i] in digits:
            number = ""
            while expression[i] in digits:
                number = number + expression[i]
                i += 1
            tokens.append(number)
        else:
            raise ValueError("Malformed Input")
    return tokens

class Expression():
    def __init__():
        self.left = None
        self.right = None
        self.operator = None

def parse(expression, index):

    if expression[index] in digits:
        number = ""
        while expression[index] in digits:
            number = number + expression[index]
            index += 1
        return int(number)

    if expression[index] == '(':
        # get sub expressions and operator
        paren_count = 1
        while True:
            index += 1
            if expression[index] == '(':
                paren_count += 1
            if expression[index] == ')':
                paren_count -= 1
                if paren_count == 0:
                    break
        index += 1
        operator = expression[index]
        left = parse(expression)

def main():
    print tokenize(sys.argv[1])

if __name__ == "__main__":
    main()

