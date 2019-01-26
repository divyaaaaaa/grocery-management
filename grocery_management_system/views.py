def view_stock_availability(stock):
    print("Item Code \t Item name \t Quantity \t Price")
    for key, value in stock.iteritems():
        print(key, "\t", value.name, "\t", value.quantity, "\t", value.price)


def view_bill(bill):
    print("Final Bill:", bill)


def view_total_sales(total_sales_obj):
    print(total_sales_obj)
