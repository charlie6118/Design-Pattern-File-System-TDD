import os
from src.node_operation import NodeOperation
from src.node_management import NodeManagement

class Folder(NodeOperation, NodeManagement):
    def __init__(self, path):
        NodeManagement.__init__(self, path)
        self.node = []

    class FolderIterator:
        def __init__(self, folder):
            self.folder = folder
            self.currentPosition = 0
        def first(self):
            self.currentPosition = 0
        def next(self):
            self.currentPosition = self.currentPosition + 1
            if self.currentPosition >= len(self.folder.node) and self.currentPosition != 0:
                self.currentPosition = len(self.folder.node)-1
        def isDone(self):
            if self.currentPosition != 0:
                return self.currentPosition == len(self.folder.node) - 1
            return False
        def currentItem(self):
            if self.currentPosition > len(self.folder.node)-1:
                return self.folder.node[-1]
            return self.folder.node[self.currentPosition]

    def add(self, node):
        self.node.append(node)

    def numberOfNodes(self):
        return len(self.node)

    def getChild(self, node_name):
        for node in self.node:
            if node_name == node.getName():
                return node
        return None

    def delete(self, node_name):
        for node in self.node:
            if node_name == node.getName():
                self.node.remove(node)

    def byCount(self):
        bc = 0
        for node in self.node:
            bc += node.byCount()
        return bc

    def createIterator(self):
        return self.FolderIterator(self)

    def getType(self):
        return "Folder"

    def getItems(self):
        return self.node
