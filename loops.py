#This section uses the for loop from lists and return a string for each item.

print("\nUsing for loop for lists.\n")

devices = ['m_phone', 'laptop', 'computer', 'tablet']
for device in devices:
    print(f"You got a {device.title()}!")
    print(f"You got another {device.title()}!\n")

print("Wow you really tried to win!")
print("\nList of number using for loop and range function.")
#using for loop  with range to print numbers
for numbers in range(0, 11):
    print(numbers)


numbers= list(range(0,11))
print(numbers)


thirdnumbers=list(range(0,34,3))
print(thirdnumbers)


print("\n\nA more complicated loop,")

squarednumbers=[]
for squarednumber in range(0,21):
    squarednumbers.append(squarednumber **2)

print(squarednumbers)

guineas=['browny', 'karma']
guineas.append('hairy')

for guinea in guineas:
    print(f"{guinea.title()}! You got this!")

added_by_fives=[]
for addition in range(0,100):
    added_by_fives.append(addition * 5)

print(added_by_fives)




#In python can use min, max, and sum for a list
numeros=[1,2,3,4,5,6,7,8]

print(numeros[1:3])





#Using a list comprehension a more advanced version for for putting for loops and elements in one line.
print("\nList Comprehension ")
heroes=[hero*3 for hero in range(0,11)]
print(heroes)
print(heroes[1:5])
print(heroes[:5])
print(heroes[0:5])
print(heroes[5:])
print(heroes[-5:])


new_characters=['scorpion', 'sub_zero', 'raiden','sonia','baraka']
print("\nThe new characters are:")

for new_character in new_characters[:3]:
        print(new_character.title())



old_characters=['scorpion', 'sub_zero', 'raiden','sonia','baraka']
print("\nThe old characters are:")
for old_character in old_characters[-2:]:
    print(old_character)



friends_old_characteres=old_characters[:]
old_characters.insert(5,'lu_kang')
print('\nThese are the old characters:')
print(old_characters)

print("\nThese are my friends old characters:")
friends_old_characteres.insert(1,'reptile')
print(friends_old_characteres)





print('\nNext is information about Tuples')

squares=(1,3,4,5)
print(squares[1])

for square in squares:
    print(square)

print('\n')
squares=(2,6,3)
for square in squares:
    print(square)









