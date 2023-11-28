from z3 import *
import random
from structure_Node import Node


'''
class Node:
    def __init__(self, value_var):
        self.value = value_var
        self.left = None
        self.right = None
'''

def collect_all_nodes(node):    
    nodes = [node]
    if node.left:
        nodes.extend(collect_all_nodes(node.left))
    if node.right:
        nodes.extend(collect_all_nodes(node.right))
    return nodes

def to_preorder(node, model):
    if node is None:
        return []
    current_str = str(model[node.value])
    left_str = to_preorder(node.left, model)
    right_str = to_preorder(node.right, model)
    return [current_str] + left_str + right_str

def to_postorder(node, model):
    if node is None:
        return []
    left_str = to_postorder(node.left, model)
    right_str = to_postorder(node.right, model)
    current_str = str(model[node.value])
    return left_str + right_str + [current_str]

def generate_mixed_expression(preorder, postorder):
    mixed = []
    for _ in range(len(preorder)):
        mixed.append(random.choice([preorder, postorder]).pop(0))
    return mixed

a = Node(String('a'))
b = Node(String('b'))
c = Node(String('c'))
d = Node(String('d'))
e = Node(String('e'))
f = Node(String('f'))
g = Node(String('g'))

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

s = Solver()

operators = ["+", "-", "*", "/"]
numbers = [str(i) for i in range(1, 20)]
possible_values = operators + numbers
random.shuffle(possible_values)

all_nodes = collect_all_nodes(a)
for i, node in enumerate(all_nodes):
    s.add(Or([node.value == StringVal(val) for val in possible_values]))
    for j, other_node in enumerate(all_nodes):
        if i != j:
            s.add(node.value != other_node.value)
    if node.left and node.right:
        s.add(Or([node.value == StringVal(op) for op in operators]))
    else:
        s.add(Or([node.value == StringVal(num) for num in numbers]))

possible_trees = []
