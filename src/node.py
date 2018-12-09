import os
from src.iterator import Iterator, NullIterator
from src.visitor import Visitor

class Node:
    def __init__(self, path):
        try:
            self.size = os.lstat(path).st_size
            self.name = path.split("/")[-1]
            self.path = path.split("/" + self.name)[0]
        except Exception as error:
            print("Path error.")

    def getSize(self):
        return self.size

    def getName(self):
        return self.name

    def getPath(self):
        return self.path

    def getType(self):
        pass

    def byCount(self):
        return self.size

    def add(self, node):
        return "Can't add node."

    def delete(self, node_name):
        return "Illegal Operation."

    def createIterator(self):
        return NullIterator()

    def accept(self, v):
        v.visit(self)
