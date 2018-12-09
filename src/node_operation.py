from src.iterator import Iterator, NullIterator
from src.visitor import Visitor

class NodeOperation:
    def __init__(self):
        pass

    def add(self, node):
        return "Can't add node."

    def delete(self, node_name):
        return "Illegal Operation."

    def createIterator(self):
        return NullIterator()

    def accept(self, v):
        v.visit(self)
