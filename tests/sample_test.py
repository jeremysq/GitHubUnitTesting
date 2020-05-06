def func(x):
    return x + 1

def test_example():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")
    assert func(2) == 3