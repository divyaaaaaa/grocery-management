import views
from models import Inventory, Register, Customer, Card, Cash, Store


def start():
    switch = True
    while switch:
        print("""
        1.New Checkout
        2.View Today's sale
        3.Exit/Quit
        """)
        choice = input("Greetings! Select from the menu:")
        if choice == "1":
            in_checkout = True
            while in_checkout:
                print("""
                        1.Add item Name/Code
                        2.View stock availability
                        3.Finish and get bill
                        4.Exit 
                    """)
                checkout_choice = input("Please enter option:")
                register_obj = Register()
                if checkout_choice == '1':
                    print("""
                          Enter "D" when done
                          Enter "C" if item code needs to be referred 
                          """)
                    purchased = []
                    interrupt = False
                    while not interrupt:
                        code = input("Enter item code:")
                        if code == 'd' or code == 'D':
                            interrupt = True
                            break;
                        elif code == 'c' or code == 'C':
                            item_name = input("Enter name to fetch item code:")
                            item_code = Inventory.get_item_code(item_name)
                            print('Item code:', item_code)
                        else:
                            purchased.append(code)
                    prices = Inventory.get_price_list(purchased)
                    register_obj.checkout(purchased, prices)
                    Inventory.update_stock(purchased)

                elif checkout_choice == '2':
                    stock = Inventory.get_stock()
                    views.view_stock_availability(stock)

                elif checkout_choice == '3':
                    print("""
                            1.Enter s to check if customer is senior citizen 
                            2.Enter P to check for other privileges
                            3.Press Enter key to proceed with bill generation without privilege check
                        """)
                    privilege = input('Enter option: ')
                    if privilege == 's':
                        discount_percentage = 30
                        register_obj.update_discount(discount_percentage)
                    elif privilege == 'p':
                        mobile_num = input("Enter mobile number to check for special discounts")
                        if Customer(mobile_num).checkprevilige():
                            discount_percentage = 20
                            register_obj.update_discount(discount_percentage)
                    bill = register_obj.get_bill()
                    views.view_bill(bill)
                    bill_amount=register_obj.get_bill_amount()
                    """
                        Using polymorphism to make payment using multiple methods, two sample methods used as example
                    """
                    payment_method = input('1.Cash 2.Card 3.Both')
                    payment_obj = []
                    if payment_method == '1':
                        payment_obj.append(Cash())
                    if payment_method == '2':
                        payment_obj.append(Card())
                    if payment_method == '3':
                        payment_obj.append(Cash())
                        payment_obj.append(Card())

                    for option in payment_obj:
                        option.receive_payment(bill_amount)

                    Store.update_total(bill_amount)
                    in_checkout = False
                elif checkout_choice == '4':
                    in_checkout = False

        elif choice == "2":
            views.view_total_sales(Store.get_total())
        elif choice == "3":
            switch = False
            print("\n Goodbye")
        elif choice != "":
            print("\n Not Valid Choice Try again")


if __name__ == '__main__':
    start()
