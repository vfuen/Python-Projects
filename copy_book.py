
def count_words(new_book):
    """""Counts the total amount of words in a file."""
    try:
        with open(new_book, encoding='utf-8') as nb:
            inside = nb.read()
    except FileNotFoundError:
        print(f"Sorry, the file {new_book} does not exist.")

    else:
        words = inside.split()
        count = len(words)

    print(f"The file {new_book} has about {count} words.")

    new_book = ["public speaking.txt",'gtht','efses']

    for new_books in new_book:
        count_words(new_book)
    