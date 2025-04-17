# Test Failure Output - Pytest results containing details on which tests failed and why.

# PDB (Python Debugger) - Tool to debug Python code by stepping through execution.

# Pytest Fixtures - Shared test data/state managed by Pytest.

# Pytest Plugins - Extensions that provide added Pytest functionality.

# Pytest Options - Command line flags that control Pytest test runner behavior.


# Using PDB to debug inside a test
import pdb

def test_stuff():
    x = 5 * 5
    pdb.set_trace() # Launch debugger  
    assert x == 10

# Pytest fixture providing temp directory   
import pytest

@pytest.fixture
def temp_dir():
    import tempfile
    dirpath = tempfile.mkdtemp() 
    yield dirpath
    import shutil 
    shutil.rmtree(dirpath)

# Pytest test function using fixture  
def test_using_dir(temp_dir):
    path = temp_dir.join("test.txt")
    # Use temp_dir path for test I/O
