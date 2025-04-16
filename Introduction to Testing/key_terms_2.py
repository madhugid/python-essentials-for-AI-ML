# Plain Asserts - Basic assertion statements in Python used to verify values and results.

# Test Classes - Classes that contain multiple related test methods and setup/teardown logic.

# Parametrize - Pytest decorator to run a test multiple times with different arguments.

# Setup Method - Code that runs before each test method in a Test Class.

# Teardown Method - Code that runs after each test method in a Test Class.

# Plain assert checking values  
def test_floats():
    result = 1.2 + 1.3
    assert result == 2.5
    
# Test class with setup/teardown    
class TestDivide:

    def setup(self):
        self.calculator = Calculator()

    def teardown(self):
        del self.calculator

    def test_divide_two_numbers(self):
        assert self.calculator.divide(10, 5) == 2 

# Parametrized test function 
@pytest.mark.parametrize("num", [1, 5, 10])
def test_squared(num):
    assert num * num == square(num)
