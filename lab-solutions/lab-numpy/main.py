#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.
print(np.__version__)
np.show_config()

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random((2, 3, 5))
# Other ways: np.random.rand(2, 3, 5), np.random.randn(2, 3, 5), np.random.uniform(size=(2, 3, 5))

#4. Print a.
print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5, 2, 3))

#6. Print b.
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?
print(a.size == b.size)  # True if they have the same size

#8. Are you able to add a and b? Why or why not?
try:
    a + b
except ValueError as e:
    print(e)  # Not able to add due to shape mismatch

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable "c".
c = b.transpose(1, 2, 0)

#10. Try to add a and c. Now it should work. Assign the sum to variable "d". But why does it work now?
d = a + c  # It works now because both arrays have the same shape

#11. Print a and d. Notice the difference and relation of the two arrays in terms of the values? Explain.
print("a:", a)
print("d:", d)  # d is a with 1 added to each element because c consists of ones

#12. Multiply a and c. Assign the result to e.
e = a * c

#13. Does e equal to a? Why or why not?
print(np.array_equal(e, a))  # True because multiplying by 1 doesn't change the elements

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty(d.shape)

#16. Populate the values in f. 
# For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
# If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
# If a value equals to d_mean, assign 50 to the corresponding value in f.
# Assign 0 to the corresponding value(s) in f for d_min in d.
# Assign 100 to the corresponding value(s) in f for d_max in d.
# In the end, f should have only the following values: 0, 25, 50, 75, and 100.
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100

#17. Print d and f. Do you have your expected f?
print("d:", d)
print("f:", f)

#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
# ("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
# array([[[ 'D',  'D',  'D',  'B',  'D'],
#        [ 'D',  'D',  'B',  'B',  'B'],
#        [ 'D',  'B',  'D',  'D',  'D']],
#
#       [[ 'B',  'B',  'B',  'B',  'E'],
#        [ 'D',  'D',  'D',  'D',  'D'],
#        [ 'B',  'D',   'A',  'D', 'D']]])
# Again, you don't need Numpy in this question.
f_str = np.empty(d.shape, dtype=str)
f_str[(d > d_min) & (d < d_mean)] = 'B'
f_str[(d > d_mean) & (d < d_max)] = 'D'
f_str[d == d_mean] = 'C'
f_str[d == d_min] = 'A'
f_str[d == d_max] = 'E'

print("f_str:", f_str)