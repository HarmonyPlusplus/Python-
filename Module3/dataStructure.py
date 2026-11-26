# creating list

# list = ["Harmony", 20, 7.9, True]
# print(list)

# student = ["Harmony", "Inyene", "Samuel", "Goodness"]
# print(student)

# # accessing through index
# print(student[0])

# # slicing
# print(student[2:])
# print(student[0:2])
# print(student[::-1])

# # modifying list
# student[0] = "Goody"
# print(student)

# list methods

# student.append("Chris") #Add items to the end 
# print(student)

# student.insert(1,"Chris")  #Add item to a specific position
# print(student)

# num = [1,2,3,4,5,6,7,8,9]
# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.remove(2) #removes a specifc stuff frm the list 
# print(num)

# num.clear() #Removes everything in a list 
# print(num)

# print(num.index(3)) #To know a particular item
# print(num.count(2)) #How many of that value do we have?
# num.pop(2)
# print(num)

#Slicing list
# num = [1,2,3,4,5,6,7,8,9]
# print(num[:]) #Gives all the elements in a list 
# print(num[::]) #Gives all the element in a list 
# print(num[:5]) #items of the begining to the on specified
# print(num[2:]) #Items after the specified index or number
# print(num[::2]) #Steps after the specifed index or element {skips every secon items and bring the rest}
# print(num[::]) #Prints out every other items after the number specified
# print(num[::-1]) #Counts decendingly

# # Iterating over list
# nums = [1,2,3,4,5,6,7,8,9,10]

# for num in nums:
#     print(num)

# students = ["Harmony", "Inyene", "Sam", "Goodness"]
# for student in students:
#     print(student)

# for student in enumerate(students):
#     print(student)

# # List comprehension
# list = []

# for x in range(5):
#     list.append(x**2)
# print(list)

# # Nested list
# nested = [[12,1], [2,3,5], ["Harmony",8,"Harmex"]]
# print(nested)
# print(nested[2][0])


# prices = []
# for p in range(10):
#     if p < 150:
#         prices.append(p*2)
# print(prices)

# balances = [1000, 2500, 400, 8000]

# new_balances = []
# for balance in balances:
#     new_balances.append(balance + 50)
# print(new_balances)

# Long way

# items = [100, 200, 300]

# new_items = []

# for item in items: 
#     if item == 300:
#         new_items.append(item)
# print(new_items)

# # Short way

# total = [item for item in items if item == 300]
# print(total)

# # classwork

# things = []

# for thing in range(10):
#     things.append(thing)
# print(things)

# # short

# total = [[thing**2] for thing in range(1,11)]
# print(total)


# new_items = [item for item in range(10) if item == 5]
# print(new_items)


# scores = [10,20,30,40,50,60,70,80,90,100]

# passed = [score for score in scores if score >=50]
# print(f"passed: {passed}")

# failed = [score for score in scores if score <=50]
# print(f"failed: {failed}")


# names = ["harmony", "goodness", "inyene"]
# scores = [1,2,3,4,5,6,7,8,9,10]

# bonus = [score+5 for score in scores ]
# print(bonus)

# uppercase = [name.upper() for name in names]
# print(uppercase)

# scores = [10,20,30,40,50,60,70,80,90,100]

# grades = ["A" if score >= 70 else "C" if score >= 60 else "F" for score in scores]
# print(grades)

## Nested list
# list = [[1,2,3], ["a","b","c"], [True, False]]

##List comprehension
# list1 = ["a", "b", "c"]
# list2 = [1,2,3]

# pairs = [[first, last] for first in list1 for last in list2]
# print(pairs)


##TUPLES
# list = ("Harmony", "Goodnews", "Goodness", 1, 2, 3)

# print(list[0])
# print(list[:])
# print(list[1:])
# print(list[::-1])

## TUPLES OPERATION
# concatination
# num = (1,2,3,4,5,6,7)
# letters = ("a","s","d","e","r")

# concatinate = num + letters
# concatinate = num * letters
# print(concatinate)

# items = ("hello", "hello", "how", "are", "you")
# print(items.count("hello"))
# print(items.index("hello"))

##PACKING AND UNPACKING TUPLES
# packed tuple
packed = 1,"hello", True
print(packed)

## unpacked tuples
# age, name, condition = packed
# print(age)
# print(name)
# print(condition)

## packing
# num = (1,2,3,4,5,6,7,8,9)
# first, *middle, last = num
# print(first)
# print(middle)
# print(last)

