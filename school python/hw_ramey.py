message = "Hello World"
print(message)

saying_one = "Python" 
saying_two = "is"
saying_three = "fun"
print(saying_one, saying_two, saying_three)

fruit = "apple"
veggy = "banana"
food = "cherry"
print(fruit, veggy, food, sep=",")

print("Hello,", end="")
print("world!")

print(" * \n ** \n ***")

color_one = "red"
color_two = "green"
color_three = "blue"
print(color_one, color_two, color_three, sep="-", end="!")


poem = """The sun sets in the west,
Painting the sky with hues of red,
A beautiful end to the day."""
print(poem)

sentence = "she said, \"I want food" "\tso we went to get food "
print(sentence)

print(1, 2, 3, sep= " ", end=" ")
print(4, 5, 6, sep=",")

word = "python"
width = len(word) + 4
print ('*' * width)
print(f'* {word} *')
print('*' * width)

num_one = 10
num_two = 3
sum_result = num_one + num_two
difference_result = num_one - num_two
product_result = num_one * num_two
quotient_result = num_one / num_two
print(sum_result)
print(difference_result)
print(product_result)
print(quotient_result)

len = 5.5
width = 3.2
area_result = len * width
print(area_result)

correct_anwser = 45
total_anwser = 50
percentage = (correct_anwser / total_anwser) 
print("percentage:", percentage )

item_price = 9.99
quantity = 3
tax_rate = 0.08
subtotal = item_price * quantity
late_the_tax = subtotal + tax_rate
tax = subtotal * tax_rate
tax_rounded = round(tax, 2)
total = subtotal + tax
total_rounded = round(total, 2)
print(subtotal)
print(late_the_tax)
print(tax)
print(total)
print(item_price)
print(quantity)
print(subtotal)
print (tax_rounded)
print(total_rounded)