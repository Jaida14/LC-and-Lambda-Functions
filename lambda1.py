def remainder(num): return num % 2


print(type(remainder))  # remainder is an instance of the function class
# this is how to invoke it: by calling it and giving it an argument
print(remainder(5))


def product(x, y): return x*y


print(product(2, 3))  # product is the function object that we created

# Method 1


def testfunc(num):
    return lambda x: x*num


result10 = testfunc(10)  # num is 10 and num is also 100
result100 = testfunc(100)

print(result10(9))
print(result100(9))

# Method 2


def result10(x): return x * 10
def result100(x): return x * 100


print(result10(9))
print(result100(9))


# Filter Function
numbers_list = [2, 4, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

# filter is for checking boolean values; psuedo if statement
# dont use if statement cause you CANT
filtered_list = filter(lambda x: (x > 7), numbers_list)
print(filtered_list)  # prints an object, needs to be wrapped in a list function

filtered_list = list(filter(lambda x: (x > 7), numbers_list))
print(filtered_list)


# Map Function
# method 1
def divide2(x):
    return x % 2


# map is for wanting to do an equation on a group of objects (list, dict, etc) at the same time instead of passing them through a function one at a time
mapped_list = list(map(divide2, numbers_list))
print(mapped_list)  # needs to be wrapped too


# Method 2
mapped_list = list(map(lambda x: x % 2, numbers_list))
print(mapped_list)
