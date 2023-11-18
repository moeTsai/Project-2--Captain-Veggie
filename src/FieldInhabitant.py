# Author: Hsiang-Mao Tsai
# Author: Hsin-Yang Tu
# Date: 11/18/2023
# Description: FieldInhabitant class


class FieldInhabitant:
    def __init__(self, symbol):
        """
        Initializes a new instance of the FieldInhabitant class.

        :param symbol: The symbol of the FieldInhabitant.
        :return: A new instance of the FieldInhabitant class.
        """
        self._symbol = symbol

    def get_symbol(self):
        """
        Gets the symbol of the FieldInhabitant.

        :return: The symbol of the FieldInhabitant.
        """
        return self._symbol

    def set_symbol(self, symbol):
        """
        Sets the symbol of the FieldInhabitant.

        :param symbol: The new symbol of the FieldInhabitant.
        """
        self._symbol = symbol
