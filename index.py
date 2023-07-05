def successor_programmer(node):
  """Finds the successor programmer of a given node in a binary search tree.

  Args:
    node: The node whose successor programmer is to be found.

  Returns:
    The successor programmer of `node`, or `None` if there is no successor.
  """

  if node is None:
    return None

  if node.right is not None:
    return min(node.right, key=lambda n: n.data)

  current_node = node
  while current_node.parent is not None:
    if current_node.parent.data < node.data:
      current_node = current_node.parent
    else:
      return current_node.parent

  return None
