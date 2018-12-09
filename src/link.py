import os
from src.node_operation import NodeOperation
from src.node_management import NodeManagement

class Link(NodeOperation, NodeManagement):
    def __init__(self, path, target):
        NodeManagement.__init__(self, path)
        self.target = target

    def byCount(self):
        return self.target.byCount()

    def getType(self):
        return "Link"

    def getTarget(self):
        return self.target
