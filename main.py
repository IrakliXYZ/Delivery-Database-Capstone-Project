# todo:
# setup tkinter ui
# he makes mistakes so... editable
# export to excel
# dashboard showing n of deliveries


import sqlite3, os, sys
import datetime, time

conn = sqlite3.connect('delivery_database.db')
curs = conn.cursor()


# Create the tables
curs.execute(
    """
    create table if not exists customer(
        customerID int primary key,
        name varchar(30) not null,
        phone varchar(20) not null
    );
    """
)
curs.execute(
    """
    create table if not exists payment(
        paymentID int primary key,
        payment float,
        tip float,
        total float,
        status binary
    );
     """
)
curs.execute(
    """
    create table if not exists orders(
        ordersID int primary key,
        packageorperson VARCHAR(10),
        date DATETIME
    );
    """
)
curs.execute(
    """
    create table if not exists location(
        locationID int primary key,
        address VARCHAR(45)
    );
    """
)
curs.execute(
    """
    create table if not exists pays(
        paysID int primary key,
        customerID int,
        paymentID int,
        foreign key (customerID) references customer (customerID) on delete cascade,
        foreign key (paymentID) references payment (paymentID) on delete cascade
    );
    """
)
curs.execute(
    """
    create table if not exists makes(
        makesID int primary key,
        customerID int,
        orderID int,
        foreign key (customerID) references customer (customerID) on delete cascade,
        foreign key (orderID) references orders (orderID) on delete cascade
    );
    """
)
curs.execute(
    """
    create table if not exists has(
        hasID int primary key,
        orderID int,
        paymentID int,
        foreign key (orderID) references orders (orderID) on delete cascade,
        foreign key (paymentID) references payment (paymentID) on delete cascade
    );
    """
)
curs.execute(
    """
    create table if not exists pickup(
        pickupID int primary key,
        orderID int,
        locationID int,
        foreign key (orderID) references orders (orderID) on delete cascade,
        foreign key (locationID) references location (locationID) on delete cascade
    );
    """
)
curs.execute(
    """
    create table if not exists dropoff(
        dropoffID int primary key,
        orderID int,
        locationID int,
        foreign key (orderID) references orders (orderID) on delete cascade,
        foreign key (locationID) references location (locationID) on delete cascade
    );
    """
)
conn.commit()


# Create a new order
def create_order():
    print("Creating a new order")
    print("Please enter the following information")
    
    global name, phone, address, date, destination, payment, tip, total, status

    # Get the customer's name
    while True:
        name = input("Customer's name: ")
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

#Legacy line so the SELECT line still works
curs.execute('INSERT INTO order_history (name, phone, address, date, destination, payment, tip, total, status) VALUES (?,?,?,?,?,?,?,?,?)', (name, phone, address, date, destination, payment, tip, total, status))

curs.execute('INSERT INTO customer (name, phone) VALUES (?,?)', (name, phone))
curs.execute('INSERT INTO payment (payment,tip,total,status) VALUES (?,?,?,?)', (payment, tip, total,status))
curs.execute('INSERT INTO orders (date) VALUES (?)', (date,))
curs.execute('INSERT INTO location (address) VALUES (?)', (address,))
curs.execute('INSERT INTO location (address) VALUES (?)', (destination,))

#Also have to include the commands for the other tables, but those use the IDs of the above tables which our code doesn't include yet

conn.commit()


#Note this command is still selecting from the old table
curs.execute(
	"""
	SELECT * FROM order_history
	"""
)

result = curs.fetchall();
print(result)

