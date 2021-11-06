import json

filename = "usernames.json"

with open(filename) as usr:
    usernames = json.load(usr)
print(f"Welcome back {usernames}!")