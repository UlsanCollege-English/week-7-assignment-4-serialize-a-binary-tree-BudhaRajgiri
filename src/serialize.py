# serialize.py

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    
    if root is None:
        return '#'

    vals = []

    def helper(node):
        if node is None:
            vals.append('#')
            return
        vals.append(str(node.val))
        helper(node.left)
        helper(node.right)

    helper(root)
    return ' '.join(vals)


def deserialize(data):
    
    if not data or data.strip() == '#':
        return None

    tokens = iter(data.split())

    def helper():
        try:
            val = next(tokens)
        except StopIteration:
            return None
        if val == '#':
            return None
        node = Node(_try_parse(val))
        node.left = helper()
        node.right = helper()
        return node

    return helper()


def _try_parse(s):
    """Try to parse string as int, else return as-is."""
    try:
        return int(s)
    except ValueError:
        return s
