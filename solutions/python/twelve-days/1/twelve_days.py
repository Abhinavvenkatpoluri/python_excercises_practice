def recite(start_verse, end_verse):
    dict_1 = {
        "first": "a Partridge in a Pear Tree.",
        "second": "two Turtle Doves,",
        "third": "three French Hens,",
        "fourth": "four Calling Birds,",
        "fifth": "five Gold Rings,",
        "sixth": "six Geese-a-Laying,",
        "seventh": "seven Swans-a-Swimming,",
        "eighth": "eight Maids-a-Milking,",
        "ninth": "nine Ladies Dancing,",
        "tenth": "ten Lords-a-Leaping,",
        "eleventh": "eleven Pipers Piping,",
        "twelfth": "twelve Drummers Drumming,"
    }

    days = list(dict_1)
    result = []

    for i in range(start_verse - 1, end_verse):

        verse = (
            f"On the {days[i]} day of Christmas "
            "my true love gave to me: "
        )

        gifts = []

        for j in range(i, -1, -1):
            gifts.append(dict_1[days[j]])

        if i > 0:
            gifts[-1] = "and " + gifts[-1]

        verse += " ".join(gifts)

        result.append(verse)

    return result