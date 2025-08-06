import sys
from main import subtract

def test_subtract():
    assert subtract(5, 3) == 2

if __name__ == "__main__":
    try:
        test_subtract()
        print("All tests passed")
    except AssertionError:
        print("Test failed")
        sys.exit(1) 