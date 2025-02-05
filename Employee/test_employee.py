import pytest
from Employee import Employee

@pytest.fixture
def employee():
    employee = Employee('Barnabas', 'Vidovics', 60000)
    return employee

def test_give_default_raise(employee):
    """Test give_raise method with default value"""
    employee.give_raise()
    assert employee.annual == 65000
    
def test_give_custom_raise(employee):
    """Test give_raise method with custom value"""
    employee.give_raise(10000)
    assert employee.annual == 70000
