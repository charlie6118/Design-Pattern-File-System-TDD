class Iterator:
    def __init__(self):
        pass

    def first():
        pass

    def next():
        pass

    def isDone():
        return False

    def currentItem():
        return Item

class NullIterator(Iterator):
    def __init__(self):
        Iterator.__init__(self)
        pass

    def first(self):
        pass

    def next(self):
        pass

    def isDone(self):
        return True

    def currentItem(self):
        return Item
