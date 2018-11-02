import numpy as np

# 1
vector_of_zeros = np.zeros(10,dtype=np.int)
print(vector_of_zeros)

# 2
vector_of_zeros2 = np.array([0,0,0,1,0,0,0,0,0,0])
print(vector_of_zeros2)

# 3

vector = np.full(10,14.8)
print(vector)

# 4
print(np.arange(23,39))

# 5

reversed_vector_of_zeros2 = np.flip(vector_of_zeros2)
print(reversed_vector_of_zeros2)

# 6

print(np.zeros(9,dtype=np.int).reshape(3,3))

# 7

print(np.arange(0,9).reshape(3,3))

# 8

vector = [1,2,0,0,4,0]
print(np.nonzero(vector))

# 9
vector = np.random.random((10,10))
print(vector)
print("\n"+str(vector.max()))
print("\n"+str(vector.min()))

# 10

vector = [1,2,2,1,2,5,2,1,1,2,1,1,5,5]
print(np.argmax(vector), np.argmin(vector))

# 11

vector = np.random.random(30)
print(vector, vector.mean())

# 12

vector = np.random.random((3,10))
print("\n")
print(vector,vector.mean(1),vector.mean(0))

# 13

print("\n")
print(np.pad(np.full((2,3),1),1,mode='constant'))


# 14

vector1 = np.full((5,3),2)
vector = np.full((3,2),3)

out = np.dot(vector1,vector)
print(out)


# 15


vector = np.random.randint(0,100,100)
vector1 = np.random.randint(0,100,100)
print(np.intersect1d(vector,vector1))

# 16

vector =np.random.random(10)
print(np.sort(vector,kind='quicksort'))

# 17

vector[vector.argmax()] = 0
print(vector)

# 18

vector = np.full((3,3),1).reshape(1,9)
print(vector)
print(np.ndarray.flatten(vector))

# 19

vector = np.random.randint(0,10,(4,4))
print(vector + vector.max())

# 20

vector = np.fromfile("array",dtype=np.int,sep=" ")
vector = vector - vector.min()
print(vector)
