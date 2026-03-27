thisdict = { 
    "Name": "Adii",
    "Age": 19,
    "Age": 19,
    "Education": "Intermediate",
    "Car": "BMW",
    "Gander": "Male",
    "colors": ["Red", "Yelow", "Green", "Blue"]
}

print(len(thisdict))
print(type(thisdict))
print(type(["colors"]))
print(type(["Name"]))
thisdict["Age"] = 29
thisdict.update({"Name": "Adil Khan"})
thisdict.pop("Age")
print(thisdict.get("Gander"))
# print(thisdict)


# Create a sample dictionary
# data = {"name": "Alice", "age": 30}

# # 1. Access an existing key
# print(data.get("name"))
# # Output: Alice

# # 2. Access a non-existent key (returns None by default)
# print(data.get("email"))
# # Output: None

# # 3. Access a non-existent key with a custom default value
# print(data.get("salary", "Not available"))
# # Output: Not available

student = {"Name": "Ali",
           "Age": "9",
           "Mordn": "90"}
for key, value in student.items():
    print(key, ":", value)