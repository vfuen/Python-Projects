users = {
    'cutey1': {
        'first': 'anh',
        'last': 'fuentes',
        'location': 'california',
        },
    'mercy43': {
        'first': 'andy',
        'last': 'banks',
        'location': 'mars',
        },
    'timdahtoolman09':{
        'first': 'ray',
        'last': 'gates',
        'location': 'new york'
        },
}


for username, userinfo in users.items():
    print(f"Usersername: {username}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']

    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
