class ILS:
    @staticmethod
    def get_value():
        return 0.27  # Example rate: 1 ILS = 0.27 USD

    @staticmethod
    def calculate(amount):
        return amount * ILS.get_value()


class USD:
    @staticmethod
    def get_value():
        return 3.52  # Example rate: 1 USD = 3.52 ILS

    @staticmethod
    def calculate(amount):
        return amount * USD.get_value()
