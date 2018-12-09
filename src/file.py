import os
from src.node_operation import NodeOperation
from src.node_management import NodeManagement


class File(NodeOperation, NodeManagement):
    def __init__(self, path):
        NodeManagement.__init__(self, path)

    def getType(self):
        return "File"
