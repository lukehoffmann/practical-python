#! /c/ProgramData/Anaconda3/python
# report.py
#
# Exercise 4.1

class Stock:

    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)


    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'


    @property
    def shares(self):
        return self._shares


    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value


    @property
    def cost(self):
        return self.shares * self.price


    def value(self, current_price):
        return self.shares * current_price


    def sell(self, number):
        self.shares -= number
