DIGITS = '0123456789'
OPERATORS = '+-*/^%'


class Node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data=None, left=None, right=0):
        self.data = data
        self.left = left
        self.right = right


def tokenize(base):
    tokens = []
    base.replace(' ', '')
    idx = 0
    while idx < len(base):
        ch = base[idx]
        if ch in DIGITS or ch in OPERATORS:
            tokens.append(ch)
        elif ch is '(':
            token = []
            idx += 1
            ch = base[idx]
            while ch is not ')':
                token.append(ch)
                idx += 1
                ch = base[idx]
            tokens.append(token)
        idx += 1
    return tokens


def main():
    s = input('Input expression >> ')
    print(tokenize(s))


if __name__ == '__main__':
    main()
