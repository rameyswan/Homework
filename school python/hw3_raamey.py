fruits = ["apple", "strawberry","orange", "peaches"]
print(fruits)


fruits[0] = "grapes"
print(fruits)


fruits.append("watermelon")
print(fruits)


fruits.insert(3, "orange")
print(fruits)


fruits.remove("orange")
print(fruits)


fruits.pop()
print(fruits)




numbers = [1, 2, 3, 4, 5, 6]
print(numbers[:3])
print(numbers[3:])


fruit = ["apple", "lemon", "lime", "banana", "grapes"]
print(fruit)


def create_fruit_list(*fruit):
    return[*fruit]


result = create_fruit_list("apple", "lemon", "lime", "banana", "grapes")
print(result, "function")


print(fruit[0])
print(fruit[2])
print(fruit[-1])


def get_fruits(fruits_list):
    return[fruits_list]
fruit_list = fruit


print(fruit_list[0])
print(fruit_list[2])
print(fruit_list[-1])






def replace_fruit(fruits_list, index, new_fruit):
    fruit_list[index] = new_fruit
    return[fruits_list, new_fruit]
new_fruit = replace_fruit(fruit, 1, "blueberry")
print(new_fruit)


fruit.append("fig")
print(fruit)


def add_fruit(fruit_list, new_fruit):
   fruit_list.append(new_fruit)
   return fruit_list


result = add_fruit(fruits, "fig")
print(result)


fruit.insert(0, "peaches")
print(fruit)


def insert_fruit(fruits_list, index, new_fruit):
    fruits_list.insert(index, new_fruit)
    return fruits_list
result = insert_fruit(fruits, 0, "grape")
print(result)


fruit.insert(3, "cherry")
print(fruit)




def remove_fruit(fruits_list, fruit_to_remove):
    fruit_to_remove = fruits_list.remove("cherry")
    return fruit_to_remove
result = remove_fruit(fruit, "cherry")
print(result)

# Step 1: Define the function to pop a fruit from the list
def pop_fruit(fruits_list, index=-1):
    """
    Remove and return the fruit at the specified index from the list.
    
    Parameters:
    - fruits_list (list): The list of fruits.
    - index (int): The index of the fruit to remove. Default is -1 (last item).
    
    Returns:
    - The fruit removed from the list.
    """
    return fruits_list.pop(index)

fruits = ['apple', 'banana', 'cherry', 'date']

removed_fruit = pop_fruit(fruits)

print(f"Removed fruit: {removed_fruit}")
print(f"Updated list: {fruits}")

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
some_fruits = fruits[:3]
print(f"Some fruits: {some_fruits}")

def slice_fruits(fruits_list, start, end):
    """
    Extract and return a slice of the list from start to end index.
    
    Parameters:
    - fruits_list (list): The list from which to slice.
    - start (int): The starting index for the slice (inclusive).
    - end (int): The ending index for the slice (exclusive).
    
    Returns:
    - A slice of the list from start to end index.
    """
    return fruits_list[start:end]

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
some_fruits = slice_fruits(fruits, 0, 3)
print(f"Some fruits: {some_fruits}")


fruits = ['apple', 'banana', 'cherry', 'date']
number_of_fruits = len(fruits)
print(f"Number of fruits: {number_of_fruits}")

def get_fruit_length(fruits_list):
    """
    Return the number of items in the list.
    
    Parameters:
    - fruits_list (list): The list to check the length of.
    
    Returns:
    - int: The number of items in the list.
    """
    return len(fruits_list)

fruits = ['apple', 'banana', 'cherry', 'date']
number_of_fruits = get_fruit_length(fruits)
print(f"Number of fruits: {number_of_fruits}")


fruits = ['banana', 'apple', 'cherry', 'date']
fruits.sort()
print(f"Sorted list of fruits: {fruits}")

def sort_fruits(fruits_list):
    """
    Sort the list of fruits in alphabetical order.
    
    Parameters:
    - fruits_list (list): The list to be sorted.
    
    Returns:
    - None: The function sorts the list in place.
    """

    fruits_list.sort()

fruits = ['banana', 'apple', 'cherry', 'date']
sort_fruits(fruits)
print(f"Sorted list of fruits: {fruits}")

fruits = ['apple', 'banana', 'cherry', 'date']
fruits.reverse()
print(f"Reversed list of fruits: {fruits}")

def reverse_fruits(fruits_list):
    """
    Reverse the order of elements in the list.
    
    Parameters:
    - fruits_list (list): The list to be reversed.
    
    Returns:
    - None: The function reverses the list in place.
    """

    fruits_list.reverse()


fruits = ['apple', 'banana', 'cherry', 'date']
reverse_fruits(fruits)
print(f"Reversed list of fruits: {fruits}")

