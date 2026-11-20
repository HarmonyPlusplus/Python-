student = {
    "name": "Goodnews",
    "department": "computer Science",
    "skill": "Software Engineer",
    "age": 20
}

student["height"] = 7.0
student["age"] = 19
del student["name"]
print(student)
# print(student["name"])
print(student["department"])


student = {}

student["name"] = "Harmony"
student["age"] = 10
student["skill"] = "Software Engineer"

print(student)

student = {}

student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["skills"] = input("What skill do you have?: ")

print(student)