#Functions printing and returning 
#print something ina function, its only for display 
# some data, you are doing nothing with the data

#when you return in a function, you are going to use 
#in another part of your program 
from add_fruit import add_fruit
from divide_fruit import divide_fruit
from subtract_fruit import subtracted_fruit


apples = int(input("how many apples?"))
oranges = int(input("how many oranges?"))
#whenever you return items, you must put the 
#returned value inside of a varible
#add fruit
fruitAdded = add_fruit(apples, oranges)
print(fruitAdded)
#subtract fruit
sub = subtracted_fruit(apples, oranges)
print(sub)
#divide fruit
div = divide_fruit(apples, oranges)
print(div)
#display the added fruit, subtracted fruit, and divided fruit
display_fruit(fruitAdded, sub, div)