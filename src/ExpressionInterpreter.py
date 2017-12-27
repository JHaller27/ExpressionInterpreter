DIGITS = '0123456789.'
OPERATORS = '+-*/^%'


class Node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data=None, left=None, right=None):
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


def generate_tree(tokens: list) -> Node:
    # Priorities: +-=0, */=1, ^=2, ()=3, digit=4
    priorities = []

    # If only token is a list (ie parens), treat as own list
    if len(tokens) == 1 and type(tokens[0]) is list:
        tokens = tokens[0]

    # Assign priorities in parallel list
    for idx, val in enumerate(tokens):
        pri = 4
        if type(val) is list:
            pri = 3
        elif val in '^':
            pri = 2
        elif val in '*/%':
            pri = 1
        elif val in '+-':
            pri = 0
        priorities.append(pri)

    # Determine first item with lowest priority
    least_priority = 4
    least_idx = 0
    for idx, pri in enumerate(priorities):
        if pri < least_priority:
            least_idx = idx
            least_priority = pri

    # Create node
    data = tokens[least_idx]
    left = generate_tree(tokens[:least_idx]) if len(tokens[:least_idx]) > 0 else None
    right = generate_tree(tokens[least_idx + 1:]) if len(tokens[least_idx + 1:]) > 0 else None
    return Node(data, left, right)


def main():
    s = input('Input expression >> ')
    tokens = tokenize(s)
    print(tokens)
    tree = generate_tree(tokens)
    print(tree)


if __name__ == '__main__':
    main()
