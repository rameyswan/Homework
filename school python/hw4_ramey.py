fruits = "apple", "banana", "cherry"
print(fruits)
print(fruits[1])

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x)
print(y)
print(z)

numbers = (1, 2, 2, 3, 4, 4, 5)
count_of_4 = numbers.count(4)
print("number 4 appears:", count_of_4, "times")
index_of_3 = numbers.index(3)
print("the first occurence of 3 is at the index:", index_of_3)

tuple1 = (1,2,3)
tuple2 = (1,2,4) 
greater_than = tuple1 > tuple2
less_than = tuple1 < tuple2
equal_to = tuple1 = tuple2
print("tuple1 > tuple2", greater_than)
print("tuple1 < tuple2", less_than)
print("tuple1 = tuple2", equal_to)

nested_tuple = (1,2,(3,4),5)
third_element_inner_tupple = nested_tuple[2][1]
print(third_element_inner_tupple)

def create_fruit_tuple():
    fruit_tuple = ('apple', 'banana', 'cherry')
    return fruit_tuple
    create_fruit_tuple()
result = create_fruit_tuple()
print(result)

def create_coordinates():
    coordinates = (10, 20, 30)
    return coordinates
    create_coordinates()
result = create_coordinates()
print(result)

def create_number_tuple():
    number_tuple = (5, 12, 7, 5, 8, 12, 3)
    return number_tuple
    create_number_tuple()
result = create_number_tuple()
print(result)

def create_comparable_tuples():
    tuple1 = (1, 4, 7)
    tuple2 = (2, 5, 8)
    return tuple1, tuple2
    create_comparable_tuples()
result = create_comparable_tuples()
print(result)

def create_nested_tuple():
    nested_tuple = (
        ('apple', 'banana', 'cherry'),
        (1, 2, 3),
        ('red', 'yellow', 'green')
    )
    return nested_tuple
    create_nested_tuple()
result = create_nested_tuple()
print(result)

student = {
    "name" : "John Doe",
    "age" : 20,
    "major" : "computer science"
}
print(student["major"])
student["gpa"] = 3.5
student["age"] = 21
del student["major"]
print("updated list", student)

fruits = {
    "apple" : 5,
    "banana" : 3,
    "orange" : 2
}
print(fruits.keys())
print(fruits.values())
print(fruits.items())

school = {
    "name" : "springfield high",
    "students": {
        "alice" : {"age": 16, "grade": 10},
        "bob" :{"age" : 17, "grade" : 11}
        }
}
print(school["students"]["bob"]["age"])
school["students"]["charlie"] = {"age": 17, "grade": 9}
print(school)

squares = {x: x**2 for x in range(1, 6)}
print(squares)

def create_person(name, age, city):
    return {
        "name": "Jazz",
        "age": 23,
        "city": "chicago"
}

def update_stock(inventory, item, quantity):
    if item in inventory: 
        inventory[item]+= quantity 
    else: 
        inventory[item] = quantity 
    return inventory

def print_person_info(person):
    name = person.get('name', 'Uknown')
    age = person.get('age', 'Uknown')
    city = person.get('city' 'Ukown')
    print(f"name: {Jazz}")
    print(f"age: {27}")
    print(f"city: {Chicago}")

def calculate_total(prices, **quantities):
    total_cost = 0.0
    
    for item, quantity in quantities.items():
        if item in prices:
            total_cost += prices[item] * quantity
        else:
            raise ValueError(f"Price for item '{item}' not found.")
    
    return total_cost

def filter_dict(d, condition):
     return {k: v for k, v in d.items() if condition(k, v)}
sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }
def condition(k, v):
    return v % 2 == 0 
filtered_dict = filter_dict(sample_dict, condition)
print(filtered_dict)
