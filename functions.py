"""functions.py
Definice matematických funkcí pro vizualizaci.
"""
import numpy as np

def linear(x, a=1.0, b=0.0):
    """Lineární funkce: f(x) = a*x + b"""
    return a * x + b

def quadratic(x, a=1.0, b=0.0, c=0.0):
    """Kvadratická funkce: f(x) = a*x^2 + b*x + c"""
    return a * x**2 + b * x + c

def sine(x, k=1.0):
    """Sinus: f(x) = sin(k*x)"""
    return np.sin(k * x)

def cosine(x, k=1.0):
    """Kosinus: f(x) = cos(k*x)"""
    return np.cos(k * x)

def exponential(x, k=1.0):
    """Exponenciální funkce: f(x) = exp(k*x)"""
    return np.exp(k * x)

def custom(x, a=1.0):
    """Vlastní funkce: f(x) = x * sin(a*x)"""
    return x * np.sin(a * x)
