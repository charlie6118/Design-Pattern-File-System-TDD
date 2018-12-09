from src.file import File
from src.folder import Folder
from src.link import Link
from src.visitor import Visitor

class FindVisitor(Visitor):
    def __init__(self, name):
        self.name = name
        self.result = ""
        self.pathStack = []

    def findName(self, node):
        if len(self.pathStack) == 0:
            self.pathStack.append(node.getPath())

        self.pathStack.append(node.getName())

        if node.getName() == self.name:
            currentPath = ""
            for path in self.pathStack:
                currentPath += path + "/"
            self.result = self.result + currentPath[:-1] + "\n"

    def visit(self, node):
        if node.getType() == "File":
            self.findName(node)
            self.pathStack.pop()

        if node.getType() == "Folder":
            self.findName(node)

            it = node.getItems()
            for item in it:
                item.accept(self)

            self.pathStack.pop()

        if node.getType() == "Link":
            self.findName(node)
            if node.getTarget().getType() == "Folder":
                it = node.getTarget().getItems()
                for item in it:
                    item.accept(self)

            self.pathStack.pop()

    def getResult(self):
        print(self.result)
        return self.result
