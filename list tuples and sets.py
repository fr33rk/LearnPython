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
# append to the end
x[len(x):] = ["kiwi", "mango", "papaya"]
print(x)
#append to the start
x[:0] = ["pineapple", "watermelon"]
print(x)

# more readable way to append
x.append("coconut")
print(x)
x.extend(["peach", "pear"])

#deleting
y = x[:]
print(f"deleting{y[:3]}")
y[:3] = []
print(y)

# reverse
x.reverse()
print(x)

#exercise append
print("exercise append")
print(f"before: {x}")
x[:0] = x[-3:]
x[-3:] = []
print(f"after: {x}")

# sort
x.sort()
print(x)
x.sort(reverse=True)
print(x)

# nested sort
y = [["apple", 41], ["apple", 50], ["banana", 2], ["banana", 1], ["grape", 3]]
y.sort(reverse=True)
print(y)

# custom sort
def sort_second(item):
    return item[2]

x.sort(key=sort_second)
print(x)

# lambda sort
x.sort(key=lambda item: item[1])
print(x)

y = sorted(x)
print(y)

#exercise sort
print("exercise sort")
x = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
x.sort(key=lambda item: item[1])
print(x)