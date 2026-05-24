"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    my_list = []

    for i in range(0, 3):
        list_rounds = number + i
        my_list.append(list_rounds)

    return my_list


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    total = 0

    for item in hand:
        total = total + item

    return total / len(hand)


def approx_average_is_average(hand):

    middle = hand[len(hand) // 2]

    first_last_average = (hand[0] + hand[len(hand) - 1]) / 2

    actual_average = card_average(hand)

    return middle == actual_average or first_last_average == actual_average


def average_even_is_average_odd(hand):

    odd_list = []
    even_list = []

    for i in range(0, len(hand)):

        if i % 2 == 0:
            even_list.append(hand[i])

        else:
            odd_list.append(hand[i])

    return card_average(odd_list) == card_average(even_list)

def maybe_double_last(hand):
    if hand[len(hand)-1] == 11:
       double= hand[len(hand)-1]*2
       hand.pop()
       hand.append(double)
    return hand