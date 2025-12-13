import math

# Basic Operations
def add(a, b):
    """Addition of two numbers"""
    return a + b

def subtract(a, b):
    """Subtraction of two numbers"""
    return a - b

def multiply(a, b):
    """Multiplication of two numbers"""
    return a * b

def divide(a, b):
    """Division of two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def min(a, b):
    """Return minimum of two numbers"""
    return a if a < b else b

# Advanced Operations
def logarithm(x, base=math.e):
    """Calculate logarithm of x with given base (default natural log)"""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(x, base)

def square(x):
    """Calculate square of a number"""
    return x ** 2

def sine(x):
    """Calculate sine of x (in radians)"""
    return math.sin(x)

def cosine(x):
    """Calculate cosine of x (in radians)"""
    return math.cos(x)

def square_root(x):
    """Calculate square root of a number"""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def percentage(value, total):
    """Calculate percentage: (value/total) * 100"""
    if total == 0:
        raise ValueError("Total cannot be zero")
    return (value / total) * 100
