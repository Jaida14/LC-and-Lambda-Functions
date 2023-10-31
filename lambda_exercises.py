''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: (x % 2 == 0), numbers_list))
print(even_numbers)

odd_numbers = list(filter(lambda x: (x % 2 != 0), numbers_list))
print(f'{odd_numbers}\n')




''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

special_days = list(filter(lambda x: len(x) == 6, weekdays))
print(f'{special_days}\n')








''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

o_g = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove = ['orange', 'black']

new_list = list(filter(lambda x: x not in remove, o_g))
print(f'{new_list}\n')











''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

new_list2 = list(filter(lambda x : x not in list2, list1 ))
print(f'{new_list2}\n')





''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

o_g2 = ['red', 'black', 'white', 'green', 'orange']

# element1 = list(map(lambda x: x.split(), o_g2))
# checking to see within each element, not as a list
element1 = list(filter(lambda x: 'ack' in x, o_g2))
print(element1)

element1 = list(filter(lambda x: 'abc' in x, o_g2))
print(f'{element1}\n')

# element1 = list(map(lambda x: x.split(), o_g2))
"""element1 = list(filter(lambda x: len(x) == 'abc', o_g2))
print(element1)"""




'''check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"

str1 = ["Hello8world", "HELLO", "hello"]

result = list(filter(lambda x: len(x) >= 8 and any(i.isupper() for i in x) and any(
    i.islower() for i in x) and any(i.isdigit() for i in x), str1))
# puts all the str into one list
print(f'{result}\n')






''' 7) 
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90),
                   ('Maths', 97), ('Social sciences', 82)]

# sort by the key which is every x element's 1st element
result = sorted(original_scores, key=lambda x: x[1])
print(f'{result}\n')




