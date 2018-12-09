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

def test_fixture(hello_cpp, test_data, folder_1):
    assert hello_cpp.getSize() == 83
    assert test_data.getSize() == 0
    assert folder_1.byCount() == 8432
    nHello_cpp = test_data.getChild("hello.cpp")
    assert nHello_cpp.getSize() == 83

def test_FileSize(hello_cpp):
    assert hello_cpp.getSize() == 83

def test_FileNotExist():
    assert File("ss"), "Path error."

def test_NodeAsObject():
    test_data = Folder("E:/Course/Design Pattern/DP_inclass/test_data")
    folder_1 = Folder("E:/Course/Design Pattern/DP_inclass/test_data/folder_1")
    hello_cpp = File("E:/Course/Design Pattern/DP_inclass/test_data/hello.cpp")

    test_data.add(folder_1)
    test_data.add(hello_cpp)

    assert test_data.numberOfNodes() == 2

def test_Name(hello_cpp, test_data, hello):
    assert hello_cpp.getName() ==  "hello.cpp"
    assert test_data.getName() == "test_data"
    assert hello.getName() == "hello"

def test_GetChild(test_data):
    nHello_cpp = test_data.getChild("hello.cpp")
    assert nHello_cpp.getSize() == 83

def test_DeleteChild(test_data):
    test_data.delete("hello.cpp")
    assert test_data.getChild("hello.cpp") ==  None

def test_AddNodeToFileReturnError(hello_cpp):
    assert hello_cpp.add(Folder("E:/Course/Design Pattern/DP_inclass/test_data/folder_1")), "Can't add node."

def test_FileByCount(hello_cpp):
    assert hello_cpp.byCount() == 83

def test_FolderByCount(test_data, folder_1):

    assert test_data.byCount() == 83 + 8432 + 8432
    assert folder_1.byCount() == 8432

def test_LinkTest(test_data, hello):

    assert hello.byCount() == 8432
    assert test_data.byCount() == 83 + 8432 + 8432

def test_path(hello_cpp, hello, folder_1):
    assert hello_cpp.getPath() == "E:/Course/Design Pattern/DP_inclass/test_data"
    assert hello.getPath() == "E:/Course/Design Pattern/DP_inclass/test_data"
    assert folder_1.getPath() == "E:/Course/Design Pattern/DP_inclass/test_data"
