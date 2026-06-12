def label(colors):
    values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    number = (values[colors[0]] * 10 + values[colors[1]]) * (10 ** values[colors[2]])

    count = 0
    temp = number

    while temp >= 1000:
        temp //= 1000
        count += 1

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]

    return f"{temp} {units[count]}"
          