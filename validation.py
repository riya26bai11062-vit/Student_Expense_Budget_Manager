def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_id(message):
    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a valid ID.")

        except ValueError:
            print("Invalid input. Please enter a number.")