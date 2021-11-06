meats=['lobster', 'beef', 'crab', 'chicken', 'squid']

for meat in meats:
        if meat == 'lobster':
                print(meat.upper())
        else:
                print(meat.title())


plush_toy='totoro'

if plush_toy != 'totoro':
        print('\nHey this is not the right plush toy!!')
else:
        print(f'\nYes, this is a {plush_toy.title()} plush toy.')


age=21
if age >= 22:
        print(f"\nTim is {age} years old.")
else:
        print("\nWrong age.")


grade_1=80
grade_2=80

print("\nAnd checks if both statements are true the true else false.")
(grade_1 >= 80) and (grade_2 >= 80)

print("\nWith or if ate least one of the statements are true, then the result will be true else false.")
(grade_1 <= 70) or (grade_2 <= 40)


#This is an example of using the keyword in to check to see if an item exists within the variable.
print("\nUsing the keyword in to check if an item exist within a variable.")
papers= [100, 390, 500, 900]
100 in papers




