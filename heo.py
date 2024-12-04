import numpy as np

# Create arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Perform element-wise operations
sum_array = a + b
product_array = a * b
dot_product = np.dot(a, b)

print(f"Array A: {a}")
print(f"Array B: {b}")
print(f"Element-wise Sum: {sum_array}")
print(f"Element-wise Product: {product_array}")
print(f"Dot Product: {dot_product}")

