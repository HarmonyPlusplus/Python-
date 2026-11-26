# roles = {
#     "frontend" : "Harmony",
#     "backend" : "Harmony.",
#     "fullstack" : "Harmony++",
#     "ceo" : {
#         "company1" : "Harmex",
#         "company2" : "HarHomes"
#     }
# }

# # print(roles["ceo"] ["company2"] )

# for position, person in roles.items():
#     print(f"{position} : {person}")



students = {
    "name":"Harmony", 
    "age":20, "country": 
    "Nigeria", 
    "beautiful" : True, 
    "height": 5.4 
}

# print(students["name"])
# # modify
# students["school"] = "FutureLabs"
# print(students)

# # update
# students["age"] = 21
# print(students)

# # deleting
# del students["beautiful"]
# print(students)

# # Dictionary Methods
# key = students.keys()
# print(key)

# values = students.values()
# print(values)

# items = students.items()
# print(items)

## Iterating over dictionary
# for key in students.keys():
#     print(key)

# for value in students.values():
#     print(value)

# for item in students.items():
#     print(item)


# # NESTED DICTIONARY
# students_collection = {
#     "students1": {
#         "name":"Harmony", 
#         "age":20, "country": 
#         "Nigeria", 
#         "beautiful" : True, 
#         "height": 5.4 
#     },
#     "students2": {
#         "name":"Harmony", 
#         "age":20, "country": 
#         "Nigeria", 
#         "beautiful" : True, 
#         "height": 5.4 
#         },
# }

# print(students_collection)

for keys, values in students.items():
    print(f"{keys}, {values}")

for values in students.values():
    print(f" values:{values}")