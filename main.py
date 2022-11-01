# todo:
# setup tkinter ui
import sqlite3, os, sys
import datetime, time

conn = sqlite3.connect('delivery_database.db')
curs = conn.cursor()



# Create a table
curs.execute(
    """
     CREATE TABLE IF NOT EXISTS order_history (
         id integer PRIMARY KEY,
         name text,
         phone integer,
         address text,
         date datetime,
         destination text,
         payment float,
         tip float,
         total float,
         status boolean
     );
     """
)
conn.commit()


global name
phone = ""
address = ""
date = ""
destination = ""
payment = ""
tip = ""
total = ""
status = ""

# Create a new order
def create_order():
    print("This is v3 running. Creating a new order")
    print("Please enter the following information")

    # Get the customer's name
    while True:
        global name = input("Customer's name: ")
        if name == "":
            print("Please enter a name")
        else:
            break

    # Get the customer's phone number
    while True:
        phone = input("Customer's phone number: ")
        if phone == "":
            print("Please enter a phone number")
        else:
            break

    # Get the pickup address
    while True:
        address = input("Pickup address: ")
        if address == "":
            print("Please enter a pickup address")
        else:
            break

    # Order date
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the destination address
    while True:
        destination = input("Destination address: ")
        if destination == "":
            print("Please enter a destination address")
        else:
            break

    # Get the customer's payment method
    while True:
        payment = input("Customer's payment method: ")
        if payment == "":
            print("Please enter a payment method")
        else:
            break
            
    # Get the customer's order tip
    while True:
        tip = input("Customer's order tip: ")
        if tip == "":
            print("Please enter an order tip")
        else:
            break
            
    # Get the customer's order total
    while True:
        total = input("Customer's order total: ")
        if total == "":
            print("Please enter an order total")
        else:
            break

    # Get the customer's order status
    # make this boolean
    while True:
        status = input("Customer's order status: ")
        if status == "":
            print("Please enter an order status")
        else:
            break


create_order()

print("name:"+name+"right")

curs.execute('INSERT INTO order_history (name, phone, address, date, destination, payment, tip, total, status) VALUES (?,?,?,?,?,?,?,?,?)', (name,phone,address,date,destination,payment,tip,total,status))

conn.commit()


    # (%s,%s,%s,%s,%s,%s,%s,%s,%s)

curs.execute(
	"""
	SELECT * FROM order_history
	"""
)

result = curs.fetchall();
print(result)
