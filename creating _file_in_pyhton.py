new_file = 'numbers.txt'

with open(new_file, 'w') as file_object:
    file_object.write("Hello your numbers are not here.\n")

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I am curently studying pyhton.\n")
    file_object.write("I previously studied html, css, and java script.\n")


with open(new_file, 'a') as file_object:
    file_object.write("I really like python.\n")
    file_object.write("I like numbers too.\n")




