def get_formatted_name(first, last, **diet):
 """Return a full name, neatly formatted."""
 diet['first_name'] = first
 diet['last_name'] = last
 return diet


lucky = get_formatted_name("lana", "mike",
                           thirdname = 'lenny',
                           nickname = "jin",
                           othername = 'elky')
print(lucky)







def myfunction():
    x = 40
    y = 30
    if x > y:
     return x
    else:
     return y

print(myfunction())






def build_profile(**user_info):
    """Build a dictionary containing everything we know about a user."""
    return user_info
user_profile = build_profile(lastname= 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)






def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

while make_pizza:
    make_pizza
    (input("What pizza size?"),
    input("What would you like for your toppings?"))







def the_messages(messages, recieved):
    while messages:
        send = messages.pop()
        print(f"Sending messages...{send}")
        recieved.append(send)

def got_messages(recieved):
    print("Messages recieved:")
    for recieves in recieved:
        print(recieves)


messages= ["yo", "cool", "lose", "next"]
recieved = []

the_messages(messages[:], recieved)
got_messages(recieved)

print(messages)







def print_method(progress_print,completed_prints):

    while progress_print:
        move_model = progress_print.pop()
        print(f"Transfering print model {move_model} ....")
        completed_prints.append(move_model)


def list_printed(completed_prints):
    print("The following models have been printed:")
    for completed_print in completed_prints:
     print(completed_print)

pogress_print = ['phone case', 'robot pendant', 'dodecahedron']
completed_prints = []

print_method(pogress_print, completed_prints)
list_printed(completed_prints)

print(pogress_print)




def ask_questions(names):
    for name in names:
     question = input(f"What is your favorite movie {name.title()}? ")
     # print(question)

people = {'tam', 'tom', 'jules'}
ask_questions(people)






def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' any time you want to quit")

    f_name = input("Type your First name: ")
    if f_name == 'q':
        break
    l_name = input("Type your Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")






def the_monster(first_name, last_name, age=None):
    monster = {'first': first_name, 'last': last_name}
    if age:
        monster['age'] = age
    return monster

eva = the_monster('tome', 'henderson', age=29)
print(eva)








def describe_city(person_name, city_name):
    """Person living in a city"""
    print(f"\n{person_name.title()} lives in {city_name.title()}.\n")
describe_city("matt","tokyo")

describe_city("jill", "new york")


def shirt_1 (shirt_size, shirt_type):
    """"Size of shirt and type"""
    print(f"Size:{shirt_size}")
    print(f"Type:{shirt_type}")
shirt_1("medium", "long sleeve")

def shirt_1 (shirt_type, shirt_size="large"):
    """"Size of shirt and type"""
    print(f"Size:{shirt_size}")
    print(f"Type:{shirt_type}")
    print("I love python.")
shirt_1("t-shirt")

def shirt_1 (shirt_type, message, shirt_size="large" ):
    """"Size of shirt and type"""
    print(f"Size:{shirt_size}")
    print(f"Type:{shirt_type}")





def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')






def indentification(name):
    """This is for identifying"""
    print(f"Hi {name.title()}!")
indentification("Jill")