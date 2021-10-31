# 1. Update Values in Dictionaries and Lists

x = [[5,2,3], [10,8,9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"]
}
z = [{"x": 10, "y": 20}]


def sportLegends():
    for nums in x:
        x[1][0] = 15
        print(x)
        break
    for values in students:
        updateDict = {"last_name": "Bryant"}
        students[0].update(updateDict)
        print(students)
        break
    sports_directory["soccer"].pop(0)
    sports_directory["soccer"].insert(0, "Andres")
    print(sports_directory["soccer"])
    for values in z:
        updateDict = {"y": 30}
        z[0].update(updateDict)
        print(z)

sportLegends()
print("----------------")

# 2. Iterate Through a List of Dictionaries

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name":"Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"}
]

def iterateDictionary(list_name):
    count = 0
    for eachDict in list_name:
        while count < len(list_name):
            print(str(list_name[count]).strip("{}").replace(":"," -").replace("'",""))
            count += 1
        break

iterateDictionary(students)
print("----------------")

# 3. Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for names in some_list:
        print(names[key_name])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)
print("----------------")

# 4. Iterate Through a Dictionary with List Values

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}

def printInfo(some_dict):
    for names in some_dict:
        print(len(some_dict["locations"]), "LOCATIONS")
        index = -1
        while index < len(some_dict["locations"]):
            print(some_dict["locations"][index])
            index += 1
        print("----------------")
        print(len(some_dict["instructors"]), "INSTRUCTORS")
        index2 = -1
        while index2 < len(some_dict["instructors"]):
            print(some_dict["instructors"][index2])
            index2 += 1
        break

printInfo(dojo)