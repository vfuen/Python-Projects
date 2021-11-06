def full_names(first, last, middle=''):
    if middle:
        full = f"{first} {middle} {last}"
    else:
        full = f"{first} {last}"
    return full.title()
