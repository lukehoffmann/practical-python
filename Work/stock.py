#! /c/ProgramData/Anaconda3/python
# report.py
#
# Exercise 4.1

class Stock:

    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)


    def cost(self):
        return self.shares * self.price


    def sell(self, number):
        self.shares -= number
