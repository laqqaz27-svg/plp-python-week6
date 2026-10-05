def get_number(text):
    try:
        number = int(text)
        return number
    except ValueError:
        return "Not a number"


print(get_number("42"))
print(get_number("abc"))