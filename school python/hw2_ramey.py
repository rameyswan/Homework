def add_two_numbers(a, b):
    return a + b

result = add_two_numbers(26, 17)
print("Sum:", result)


def greet(name):
    print(f"Hello, {name}! Welcome!")

greet("Maggie")


def calculate_area(length, width):
    return length * width

length = 5
width = 3
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")


def sum_of_numbers(*args):
    return sum(args)

result1 = sum_of_numbers(1, 2, 3)
result2 = sum_of_numbers(12, 23, 34, 45)
print("Sum 1:", result1)
print("Sum 2:", result2)


def power(base, exponent):
    return base ** exponent

result = power(7, 8)
print("Result:", result)


def concatenate_strings(*args):
    return ''.join(args)

result1 = concatenate_strings("Hello", " ", "world", "!")
result2 = concatenate_strings("Live", " ", "Laugh", " ", "Love")
print("Result 1:", result1)
print("Result 2:", result2)


def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_details(name="Ramey", age=68, city="Chicago", profession="Stay at home mom")


def print_args_and_kwargs(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_args_and_kwargs(1, 2, 3, name="Maddie", age=68, city="Chicago")


def outer_function(outer_param):
    def inner_function():
        print(f"I am inside: {outer_param}")
    
    
    inner_function()

outer_function("Now I'm outside!")


x = "I am a global variable"

def demonstrate_LEGB():
    x = "I am a local variable"
    
    print(x)

print(x)
demonstrate_LEGB()
print(x)