from coins import ILS, USD


def amount(selected_currency):
    coins = valid_amount()  # Ensure the amount entered is valid

    while coins:
        if selected_currency == '1':
            result = ILS.calculate(coins)
            return result, '1'

        elif selected_currency == '2':
            result = USD.calculate(coins)
            return result, '2'


def valid_amount():
    while True:
        try:
            # Attempt to convert user input to a float
            return float(input("Enter the amount of coins to convert\n"))
        except ValueError:
            # If input is invalid, prompt again
            print("Invalid input. Please enter a valid number.")


# a, b = amount('2')
# print(a, b)
