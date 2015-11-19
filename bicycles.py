from subprocess import call
import csv
import datetime

"""Bike Industry Management System Module

Please use the classes and functions contained in this module to design you
Bicycle Industry Management needs.
"""


class Bicycle(object):
    """ This class requires three attributes when called:
        model_name as string
        weight as float in kilograms
        cost_to_produce in US dollars"""

    def __init__(self, model_name, model_description, cost_to_produce, weight):
        self.model_name = model_name
        self.model_description = model_description
        self.cost_to_produce = cost_to_produce
        self.weight = weight
        self.cost_to_produce = cost_to_produce


class Bike_Shop(object):
    """ This class requires two atributes when called:
        name as string
        margin as float
        """

    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = []
        self.customers = []
        self.transactions = []
        # build inventory
        f = open('inventory.csv', 'r', newline='')
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
        call('clear')
        for row in reader:
            print(row)
            self.inventory.append(row)

        f.close

        print('\n\n\n')

        # build customer list
        f = open('crm.csv', 'r', newline='')
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
        for row in reader:
            print(row)
            self.customers.append(row)

        f.close

        # build transaction list
        f = open('transactions.csv', 'r', newline='')
        reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
        for row in reader:
            print(row)
            self.transactions.append(row)

        f.close


    def showroom(self):
        call('clear')
        print("""model description\t\tPrice\t\tQuantity""")
        for row in self.inventory[1:]:
            print("""{}\t\t{:.2f}\t\t{}""".format(row[1],
                                                  row[2]*(self.margin+1),
                                                  row[4]))

    def show_inventory(self):
        call('clear')
        print("""{}\t{}\t{}\t{}\t{}""".format(self.inventory[0][0],
                                                      self.inventory[0][1],
                                                      self.inventory[0][2],
                                                      self.inventory[0][3],
                                                      self.inventory[0][4]))

        for row in self.inventory[1:]:
            print("""{}\t{}\t{}\t\t{}\t{}""".format
                  (row[0], row[1], row[2], row[3], row[4]))

    def crm(self):
        call('clear')
        for customer in self.customers[1:]:
            print('{}={} | {}={} | {}={}'.
                  format(self.customers[0][0], customer[0],
                         self.customers[0][1], customer[1],
                         self.customers[0][2], customer[2]))

            print('------------')

            print("""model description\t\tPrice\t\tQuantity""")

            for bike in self.inventory[1:]:
                if bike[2]*(self.margin+1) < customer[2]:
                    print("""{}\t\t{:.2f}\t\t{}""".format(bike[1],
                                                          bike[2]*(self.margin+1
                                                                   ), bike[4]))

            print('')

    def purchase(self, customer_number, model_name):
        inventory_record = ''
        customer_record = ''
        for customer in self.customers[1:]:
            if customer_number in customer:
                for bike in self.inventory:
                    if model_name in bike:
                        if customer[2] >= (bike[2]*(self.margin+1)):
                            self.transactions.append([customer[0],
                                                      customer[1],
                                                      model_name,
                                                      str(datetime.
                                                          datetime.now()),
                                                      (bike[2]*(1+self.margin))])
                            inventory_record = self.inventory.index(bike)
                            self.inventory[inventory_record][4] -= 1
                            customer_record = self.customers.index(customer)
                            self.customers[customer_record][2] = self.customers[customer_record][2] - self.inventory[inventory_record][2]*(1 + self.margin)

                            f = open('transactions.csv', 'w', newline='')
                            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
                            for row in self.transactions:
                                writer.writerow(row)

                            f.close
                            del f

                            f = open('crm.csv', 'w', newline='')
                            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
                            for row in self.customers:
                                writer.writerow(row)

                            f.close
                            del f


                            f = open('inventory.csv', 'w', newline='')
                            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, quotechar="'")
                            for row in self.inventory:
                                writer.writerow(row)

                            f.close
                            del f







