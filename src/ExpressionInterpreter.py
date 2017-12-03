DIGITS = '0123456789'
OPERATORS = '+-*/^%'


class Node:
  __slots__ = 'left, right, data'

  def Node(self):
    left = None
    right = None
    data = 0

  def Node(self, left, data, right):
    self.left = left
    self.data = data
    self.right = right

  def Node(self, data):
    self(None, data, None)


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
