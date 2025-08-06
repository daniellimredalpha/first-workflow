import sys
from main import add

def test_add():
    assert add(3, 5) == 1

if __name__ == "__main__":
    try:
        test_add()
        print("All tests passed")
    except AssertionError:
        print("Test failed")
        sys.exit(1) 