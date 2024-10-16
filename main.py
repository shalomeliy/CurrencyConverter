from welcome import welcome
from get_currency import get_currency
from amount import amount

test = '1'
test2 = '5'
replay = 'y'
welcome()
while replay == 'y':
    selected_currency = get_currency()
    result, currency = amount(selected_currency)
    print(f'\nConverted result is: {result}\n')
    replay = input("Do you want to perform another conversion? (y/n)\n")

    if replay.lower() == 'n':
        print("Thanks for using our currency converter")
        break
    elif replay.lower() == 'y':
        pass
    else:
        print("Invalid answer, please type 'y' OR 'n'")
        pass

