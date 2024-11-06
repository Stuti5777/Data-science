import numpy as np
import time

# Create a list of integers
nums = [2,8,4,3,7]
print(nums)  # Print the list
print(type(nums))  # Check and print the type of the list (should be 'list')

# Convert the list to a NumPy array
nums_arr = np.array(nums)
print(nums_arr)  # Print the NumPy array
print(type(nums_arr))  # Check and print the type of the array (should be 'numpy.ndarray')

# Multiply each element of the list by 2 using a loop
for item in nums:
    print(item*2)

# Multiply each element of the NumPy array by 2 (vectorized operation)
print(nums_arr*2)

# Measure time taken to create a list with 1 million elements
t1 = time.time()
l1 = [i for i in range(1000000)]
t2=time.time()
print("Time for list", t2-t1)

# Measure time taken to create a NumPy array with 1 million elements
t1 = time.time()
a1 = np.arange(0,1000000)
t2=time.time()
print("Time for array", t2-t1)


# Create a NumPy array of zeros with 5 elements (integers)
z1 = np.zeros(5, int)
print(z1)

# Create a NumPy array of ones with 5 rows and 2 columns (floats by default)
o1 = np.ones((5,2))
print(o1)

# Print the number of dimensions for both arrays
print(z1.ndim)  # 1D array
print(o1.ndim)  # 2D array

# Print the shape (dimensions) of both arrays
print(z1.shape)  # (5,)
print(o1.shape)  # (5, 2)

# Print the number of elements in both arrays
print(z1.size)  # 5 elements
print(o1.size)  # 10 elements (5 rows * 2 columns)

# Create a NumPy array using np.arange (start=10, stop=21, step=2)
arr1 = np.arange(10,21,2)
print(arr1)

# Create a NumPy array using np.linspace (4 equally spaced values between 10 and 21)
arr2 = np.linspace(10,21,4)
print(arr2)

# Reshape arr1 into a 3x2 matrix
new = arr1.reshape(3,2)
print(new)

# Reshape the 3x2 matrix back into a 1D array of 6 elements
one = new.reshape(6)
print(one)

# Create a random permutation of arr1 (shuffling the elements)
print(np.random.permutation(arr1))
print(np.random.permutation(arr1))
print(np.random.permutation(arr1))

# Generate 10 random integers between 1 and 50
r1 = np.random.randint(1,50,10)
print(r1)

# Randomly permute the elements of r1
print(np.random.permutation(r1))

# Save the permutation to variable n1
n1 = np.random.permutation(r1)

# Generate a 3x4 matrix with random integers between 1 and 50
r2 = np.random.randint(1,50,(3,4))
print(r2)

# Randomly permute rows of the 3x4 matrix
print(np.random.permutation(r2))

# Sort the elements of n1 in ascending order
print(n1)
print(np.sort(n1))

# Slicing the NumPy array n1
print(n1[2:7])  # Elements from index 2 to 6
print(n1[:7])   # First 7 elements
print(n1[2:])   # Elements from index 2 to the end
print(n1[::2])  # Every second element
print(n1[::-1]) # Reverse the array

# Select specific indices from the array n1
print(n1[[1,2,5,8]])

# Conditional slicing: selecting even numbers
print(n1[n1 % 2 == 0])

# Conditional slicing: selecting numbers greater than 20
print(n1[n1 > 20])

# Slicing a 2D array (r2), selecting from row 0, columns 1 to the end
print(r2[0:1, 1:])

# Define a function to calculate 2x^2 + 3 for input x
def cal(x):
    return 2*x**2 + 3

# Create a NumPy array from 1 to 10 and apply the function
n = np.arange(1,11)
print(cal(n))

# Create two NumPy arrays and perform element-wise addition, subtraction, and exponentiation
x = np.arange(1,5)
y = np.arange(11,15)
print(x+y)     # Element-wise addition
print(x-y)     # Element-wise subtraction
print(x**y)    # Element-wise exponentiation (x raised to the power of y)
