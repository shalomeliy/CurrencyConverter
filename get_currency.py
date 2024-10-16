def get_currency():
    while True:
        print("Select a currency to convert\n")
        print("1 - Shekels to Dollars\n2 - Dollars to Shekels\n")
        selected_currency = input()

        if selected_currency == '1' or selected_currency == '2':
            return selected_currency
        else:
            print("Invalid input. Please enter a valid number.\n")
            get_currency()



# get_currency()
