DIGITS = '0123456789.'
OPERATORS = '+-*/^%'


class Node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data=None, left=None, right=0):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return format('(%s <- %s -> %s)' % (self.left, self.data, self.right))


def tokenize(base):
    tokens = []
    base = base.replace(' ', '')
    idx = 0
    while idx < len(base):
        ch = base[idx]

        # Handle operator
        if ch in OPERATORS:
            tokens.append(ch)
            idx += 1

        # Handle numbers
        elif ch in DIGITS:
            token = ''
            while ch in DIGITS:
                token += ch
                idx += 1
                if idx < len(base):
                    ch = base[idx]
                else:
                    break
            tokens.append(token)

        # Handle parens
        elif ch is '(':
            paren_text = ''
            paren_num = 1
            while paren_num > 0:
                idx += 1
                ch = base[idx]
                if ch is '(':
                    paren_num += 1
                    paren_text += ch
                elif ch is ')':
                    paren_num -= 1
                    if paren_num is not 0:
                        paren_text += ch
                else:
                    paren_text += ch
            tokens.append(tokenize(paren_text))
            idx += 1
    return tokens


def main():
    s = input('Input expression >> ')
    print(tokenize(s))


if __name__ == '__main__':
    main()
