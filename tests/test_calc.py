import sys
from pathlib import Path

# Add parent directory to path so we can import from src
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.calc import add, subtract, multiply


def test_add():
    """Test the add function"""
    assert add(2, 3) == 5, "add(2, 3) should return 5"
    assert add(0, 0) == 0, "add(0, 0) should return 0"
    assert add(-5, 5) == 0, "add(-5, 5) should return 0"
    assert add(10, -3) == 7, "add(10, -3) should return 7"


def test_subtract():
    """Test the subtract function"""
    assert subtract(10, 3) == 7, "subtract(10, 3) should return 7"
    assert subtract(0, 0) == 0, "subtract(0, 0) should return 0"
    assert subtract(5, 10) == -5, "subtract(5, 10) should return -5"
    assert subtract(-5, -3) == -2, "subtract(-5, -3) should return -2"


def test_multiply():
    """Test the multiply function"""
    assert multiply(3, 4) == 12, "multiply(3, 4) should return 12"
    assert multiply(0, 100) == 0, "multiply(0, 100) should return 0"
    assert multiply(-5, 2) == -10, "multiply(-5, 2) should return -10"
    assert multiply(-3, -4) == 12, "multiply(-3, -4) should return 12"
