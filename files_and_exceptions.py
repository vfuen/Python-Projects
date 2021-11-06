with open("txt_files\pi_digits.txt") as pi_file:
    inside_file = pi_file.read()
    print(inside_file.rstrip())

print("\n")
other_files = "C:\\Users\\vfuen\\Desktop\\other_python_files\\other_text.txt"

with open(other_files) as other_f:
    for row in other_f:
        print(row.rstrip())


print("\n")

























with open("C:\\Users\\vfuen\\Documents\\Resume\\Python projects\\txt_files\\two_blocks_for_reading_a_file.txt") as block_file:
    lines = block_file.readlines()

print_like_sentence = ""
for line in lines:
    print_like_sentence += line.strip()
print(f"{print_like_sentence[:300]}....")
print(len(print_like_sentence))

print("\n")

birthday = input("Please type your birthday in the form of mmddyy ")
if birthday in print_like_sentence:
    print("Your birthday is in the first 200 of pi")
else:
    print("Your birthday is not in pi.")
