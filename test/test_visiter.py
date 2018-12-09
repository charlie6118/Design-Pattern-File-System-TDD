import pytest
from src.find_visitor import *

@pytest.fixture
def a_out2():
    return File("E:/Course/Design Pattern/DP_inclass/test_data/folder_1/folder_2/a.out")

@pytest.fixture
def folder_2(a_out2):
    folder_2 = Folder("E:/Course/Design Pattern/DP_inclass/test_data/folder_1/folder_2")
    folder_2.add(a_out2)
    return folder_2

@pytest.fixture
def a_out():
    return File("E:/Course/Design Pattern/DP_inclass/test_data/folder_1/a.out")

@pytest.fixture
def link_to_folder_2(folder_2):
    return Link("E:/Course/Design Pattern/DP_inclass/test_data/link_to_folder_2", folder_2)

@pytest.fixture
def hello_cpp():
    return File("E:/Course/Design Pattern/DP_inclass/test_data/hello.cpp")

@pytest.fixture
def hello(a_out):
    return Link("E:/Course/Design Pattern/DP_inclass/test_data/hello", a_out)

@pytest.fixture
def folder_1(a_out, folder_2):
    folder_1 =  Folder("E:/Course/Design Pattern/DP_inclass/test_data/folder_1")
    folder_1.add(a_out)
    folder_1.add(folder_2)
    return folder_1

@pytest.fixture
def test_data(link_to_folder_2, hello_cpp, hello, folder_1):
    test_data = Folder("E:/Course/Design Pattern/DP_inclass/test_data")
    test_data.add(link_to_folder_2)
    test_data.add(hello_cpp)
    test_data.add(hello)
    test_data.add(folder_1)
    return test_data


def test_FindOnFileForFile(hello_cpp):
    v = FindVisitor("hello.cpp")
    hello_cpp.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data/hello.cpp\n"

def test_FindOnFolderForFolder(test_data):
    v = FindVisitor("test_data")
    test_data.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data\n"

def test_FindOnLinkForLink(hello):
    v = FindVisitor("hello")
    hello.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data/hello\n"

def test_FindOnFolderForOneFile(test_data):
    v = FindVisitor("hello.cpp")
    test_data.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data/hello.cpp\n"

def test_FindOnFolderForLink(test_data):
    v = FindVisitor("hello")
    test_data.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data/hello\n"

def test_FindOnFolderForTwoFile(test_data):
    v = FindVisitor("a.out")
    test_data.accept(v)
    assert v.getResult() == "E:/Course/Design Pattern/DP_inclass/test_data/link_to_folder_2/a.out\nE:/Course/Design Pattern/DP_inclass/test_data/folder_1/a.out\nE:/Course/Design Pattern/DP_inclass/test_data/folder_1/folder_2/a.out\n"
