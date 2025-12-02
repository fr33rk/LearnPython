# Array asignment
x = [ 1, 2, 5]
print(x)

x = [ 2, "two", [1, 2, 5]]
print(x)
print(x[2])
print(len(x))

# Indexing
x = ["apple", "banana", "lemon", "grape", "orange", "strawberry"]
print(x[0])
print(x[-1])

print(x[1:-1])
#To but not including
print(x[1:4])
print(x[-3:-1])
print(x[:3])
print(x[3:])

# Copy
print('Copy')
y = x[:]
y[0] = "black berry"
print(x)
print(y)

# Test get the last half of the list
print(x[len(x)//2:])

# Modifying lists
