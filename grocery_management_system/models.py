class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Store:
    __total_sale = 0

    def get_total(self):
        return Store.__total_sale

    def update_total(self, payment):
        Store.__total_sale += payment


class Customer:
    __previliged_customer_numbers = [9874563211, 7845129633, 854745874]

    def __init__(self, mobile_number):
        self.mobile_number = mobile_number

    def checkprevilige(self):
        if self.mobile_number in Customer.__previliged_customer_numbers:
            return True
        return False


class Inventory:
    __stock = {}

    def __init__(self):
        __stock = self.load_items()  # Stock is made private to deny access from other modules

    @staticmethod
    def load_items(self):
        """
        Loads stock using log file
        """
        stock = {}
        with open('inventory_log.txt') as inventory_log:
            next(inventory_log)
            for line in inventory_log:
                line_list = line.split()
                stock[line_list[0]] = Item(line_list[0], line_list[1], line_list[2])
        return stock

    def get_stock(self):
        return Inventory.__stock

    def update_stock(self, purchased):
        for item_code in purchased:
            Inventory.__stock[item_code].quantity -= 1

    @staticmethod
    def get_price_list(self, item_list):
        price_list = []
        for item in item_list:
            price_list.append(Inventory.stock[item].price)
        return price_list


class Register:
    def __init__(self):
        self.__bill = 'ItemName\tPrice'
        self.__bill_total = 0

    def checkout(self, item_list, price_list):
        for i in range(0, len(item_list)):
            self.__bill += ('\n', item_list[i], '\t', price_list[i])
            self.__bill += price_list[i]
        return self.__bill_total

    def get_bill(self):
        self.__bill += ('Total:', str(self.__bill_total))

    def get_bill_amount(self):
        return self.__bill_total

    def update_discount(self, percentage):
        discount = (percentage / 100) * self.__bill
        self.__bill_total -= discount


class Payment:
    def __init__(self):
        self.payment_made = 0

    def receive_payment(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Cash(Payment):
    """
    Inherits payment class
    """

    def receive_payment(self, amount):
        print('Payment successful by cash')
        Payment.payment_made += amount


class Card(Payment):
    """
        Inherits payment class
    """

    def receive_payment(self, amount):
        print('Payment successful by card')
        self.payment_made += amount