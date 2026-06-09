"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number): 
    seats = ["A", "B", "C", "D"] 
    for i in range(number): 
        yield seats[i % 4]
    

def generate_seats(number):
    seats = ["A", "B", "C", "D"]

    count = 0
    main = 1

    while count < number:

          if main == 13:
             main += 1
             continue

          for item in seats:

              if count >= number:
                 return

              yield str(main)+item
              count += 1

          main+= 1
def assign_seats(passengers):
    new_dict = {}

    seats = generate_seats(len(passengers))

    for passenger in passengers:
        new_dict[passenger] = next(seats)

    return new_dict

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        yield seat + flight_id + "0" * (12 - len(seat) - len(flight_id))
