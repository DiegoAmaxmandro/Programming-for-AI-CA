# Importing necessary libraries
import numpy as np # type: ignore

# Initializing a random 2D array
np.random.seed(0) # Setting the inicial value
array = np.random.randint(10, 100, size=(20, 5)) #Generating the random numbers

# Looping throught it row to make it even
for i in range(array.shape[0]):
    row_sum = array[i].sum()
    if row_sum % 2 != 0:
        array[i][0] += 1


# Looping throught it row to make it multiple by 5
array_sum = array.sum()
if array_sum % 5 != 0:
    array[0][0] += (5 - (array_sum % 5))

print(f'Ajusted 2D Array: \n {array} \n')

# Ectracting and printing all elements divisible by 3 and 5
divisible_by_3_5 = array[(array % 3 == 0) & (array % 5 == 0)]
print(f'Elements divisible by 3 and 5: \n {divisible_by_3_5} \n')

# Replacing all numbers grater then 75 for the array's mean number
array_mean = array.mean()
array[array > 75] = array_mean
print(f'Array with replaced elements : \n {array} \n')

# Calculating the mean and standard deviation 
mean_value = np.mean(array)
std = np.std(array)
print(f'Mean of the array: {mean_value} \n')
print(f'Standard deviation of the array: {std} \n')

# Finding the median value of the array
median_value = np.median(array)
print(f'Median value of the array: {median_value} \n')

# Computing the variance for each column of the array
column_varicance = array.var(axis=0)
print(f'Variance for each column: {column_varicance} \n')