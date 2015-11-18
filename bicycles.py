from subprocess import call
import csv

"""Bike Industry Management System Module

Please use the classes and functions contained in this module to design you
Bicycle Industry Management needs.
"""


class Bicycle(object):
    """ This class requires three attributes when called:
        model_name as string
        weight as float in kilograms
        cost_to_produce in US dollars"""

    def __init__(self, model_name, model_description, cost_to_produce, weight,
                 quantity):
        self.model_name = model_name
        self.model_description = model_description
        self.cost_to_produce = cost_to_produce
        self.weight = weight
        self.cost_to_produce = cost_to_produce
        self.quantiy = quantity


class Bike_Shop(object):
    """ This class requires two atributes when called:
        name as string
        margin as float
        """

    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = []
        # build inventory
        f = open('data.csv', 'r', newline='')
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")

        for row in reader:
            print(row)
            self.inventory.append(row)

        f.close
        del f

