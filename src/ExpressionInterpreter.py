DIGITS = '0123456789'
OPERATORS = '+-*/^%'

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
      while ch is not ')':
        idx += 1
        ch = base[idx]
        token.append(ch)
      idx += 1
      tokens.append(token)
    idx += 1
  return tokens


def main():
    s = input('Input expression >> ')
    print(tokenize(s))


if __name__ == '__main__':
  main()
