import pytest
from src.file import File
from src.folder import Folder
from src.link import Link


@pytest.fixture
def hello_cpp():
    return File("E:/Course/Design Pattern/DP_inclass/test_data/hello.cpp")

@pytest.fixture
def a_out():
    return File("E:/Course/Design Pattern/DP_inclass/test_data/folder_1/a.out")

@pytest.fixture
def hello(a_out):
    return Link("E:/Course/Design Pattern/DP_inclass/test_data/hello", a_out)

@pytest.fixture
def folder_1(a_out):
    folder_1 =  Folder("E:/Course/Design Pattern/DP_inclass/test_data/folder_1")
    folder_1.add(a_out)
    return folder_1

@pytest.fixture
def test_data(folder_1, hello_cpp, hello):
    test_data = Folder("E:/Course/Design Pattern/DP_inclass/test_data")
    test_data.add(folder_1)
    test_data.add(hello_cpp)
    test_data.add(hello)
    return test_data


def test_FileShouldCreateNullIterator(hello_cpp):
    it = hello_cpp.createIterator()
    print(type(it))

    assert it.isDone, True
def test_TestDataHasAllThings(test_data):
    node1 = test_data.getChild("folder_1")
    assert node1.getName() == "folder_1"

    node3 = test_data.getChild("hello")
    assert node3.getName() == "hello"

    node2 = test_data.getChild("hello.cpp")
    assert node2.getName() == "hello.cpp"


def test_FolderShouldCreateFolderIterator(test_data, hello_cpp):
    it = test_data.createIterator()
    it.first()
    assert it.currentItem().getName() == "folder_1"
    it.next()
    assert it.currentItem().getName() == "hello.cpp"
    it.next()
    assert it.currentItem().getName() == "hello"
    it.next()
    assert it.isDone, True
