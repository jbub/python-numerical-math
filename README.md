# Numerical math

## Topics

* Babylonian method **babylon.py**
* Bisection method **bisection.py**
* Regula falsi method **regulafalsi.py**
* Newton method **newton.py**
* Jacobi method **jacobi.py**
* Gauss Seidel method **gaussseidel.py**
* Lagrange polynomial
* Least squares method
* Numerical integration - Rectangular method **rectangle.py**
* Numerical integration - Trapezoidal method

## How to

### Running

First insert the numa package to your PYTHONPATH. This is example on how to run the babylon.py script.

    cd numa/topics && python babylon.py

### Matrices and Vectors

```python
# input matrices as lists
[[11,2,1],[1,10,2],[2,3,-8]]

# it will generate this Matrix instance
Matrix((
    [11,2,1],
    [1,10,2],
    [2,3,-8]
))

# input vectors as one col matrices
[[15],[16],[1]]

# it will generate this Matrix instance
Matrix([
    [15],
    [16],
    [1],
])
```
