# ExpressionInterpreter
Interpret a text-based mathematical expression (eg "5+(2\*3-1)^1") and return the result

**General Algorithm**
* Remove spaces
* Tokenize - Tokens: bare #s and ops, stuff in parens
* Scan list of tokens for highest priority ops (ignore bare #s)
* Add node to tree with first token of lowest priority (following PEMDAS) as root and with entire list as children...
  * List[0:here) = left child, List(here:end] = right child
* Recurse for each child that is a list
* Evaluate w/ In Order (LVR) traversal
