# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:01:38 2023

@author: Asus
"""

#Import numpy library
import numpy as np

#Create a list and convert it to numpy array
a = [1, 2, 3, 4]
type(a)
b = np.array(a)
type(b)

#Create a 2D list and convert it to numpy array
c = [[1, 2, 3], [4, 5, 6]]
d = np.array(c)
d.shape

#Create arrays of zeros and ones with specified shape
np.zeros(3)
np.zeros((3, 5))
np.ones((2, 7))

#Create identity matrix
np.eye(6)

#Generate random numbers from uniform and normal distributions
np.random.rand(4) # Generate 4 numbers between 0 and 1
np.random.rand(3, 5)
np.random.randn(4) # Generate 4 numbers from standard normal distribution
np.random.normal(4.0, 1.0, 100) # Generate 100 random numbers based on normal distribution

#Set a random seed for reproducibility
np.random.seed(4)
np.random.rand(4)

#Create an array of integers with arange function
e = np.arange(1, 20) # Generate integers between 1 and 19
e[4] # Access element at index 4
e[6:17] # Access elements from index 6 to 16
e[6:] # Access elements from index 6 to the end
e[:6] # Access elements from the beginning to index 5

#Access elements of a 2D array and perform mathematical operations on it
d[0] # Access the first row of array d
d[0][2] # Access the element in the first row and third column of array d
d + 5 # Add 5 to each element of array d
d * 5 # Multiply each element of array d by 5
d ** 2 # Square each element of array d