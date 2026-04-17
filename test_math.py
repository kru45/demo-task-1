import math_utils

def test_add_function():
    # We check if 10 + 20 equals 30
    result = math_utils.add(10, 20)
    assert result == 30, f"Math error! Expected 30 but got {result}"
    print("Test Passed: 10 + 20 is 30")

if __name__ == "__main__":
    test_add_function()
