1# todo:
# delivery status: canceled?
# setup tkinter ui
# he makes mistakes so... editable
# export to excel
# dashboard showing n of deliveries

import sqlite3
import os
import sys
import datetime
import time
import random

conn = sqlite3.connect("delivery_database.db")
curs = conn.cursor()

name, phone, address, date, destination, cpayment, tip, total, status, type = '','','','','','','','','',''

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
        paymentAmount float,
        tip float,
        total float,
        paymentType VARCHAR(10)
    );
     """
)
curs.execute(
    """
    create table if not exists orders(
        ordersID int primary key,
        type VARCHAR(10),
        date DATETIME,
        status binary
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

    global name, phone, address, date, destination, cpayment, tip, total, status, type

    # Get the customer's name
    if name == "":
        return ("Please enter a name")

    # Get the customer's phone number
    if phone == "":
        return ("Please enter a phone number")

    # Get the pickup address
    if address == "":
        return ("Please enter a pickup address")

    # Order date
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the destination address
    if destination == "":
        return ("Please enter a destination address")

    # Get the customer's payment method
    if cpayment == "":
        return ("Please enter a payment method")

    # Get the customer's order tip
    if tip == "":
        return ("Please enter an order tip")

    # Get the customer's order total
    if total == "":
        return ("Please enter an order total")

    # Get the customer's order status
    # make this boolean
    if status == "":
        return ("Please enter an order status")

    #Get order type
    if type == "":
        return ("Please enter an order type")


# Check if the customer exists, if does retrieve customerID, if not create a new random customerID
def check_customer():
    global customerID
    curs.execute("select * from customer where name = ? and phone = ?", (name, phone))
    customer = curs.fetchone()
    if customer is None:
        customerID = random.randint(100000, 999999)
        curs.execute("insert into customer values (?, ?, ?)", (customerID, name, phone))
        conn.commit()
    else:
        customerID = customer[0]
        print("Customer already exists, customerID is", customerID)


# Check if the payment exists, if does retrieve paymentID, if not create a new random paymentID
def check_payment():
    global paymentID
    curs.execute(
        "select * from payment where paymentType = ? and tip = ? and total = ?",
        (cpayment, tip, total),
    )
    payment = curs.fetchone()
    if payment is None:
        paymentID = random.randint(100000, 999999)
        curs.execute(
            "insert into payment values (?, ?, ?, ?, ?)",
            (paymentID, float(total)-float(tip), tip, total, cpayment),
        )
        conn.commit()
    else:
        paymentID = payment[0]
        print("Payment already exists, paymentID is", paymentID)


# Check if date exists, if does retrieve dateID, if not create a new random dateID
def check_order():
    global orderID
    curs.execute("select * from orders where date = ? and status = ? and type = ?", (date, status, type))
    order = curs.fetchone()
    if order is None:
        orderID = random.randint(100000, 999999)
        curs.execute("insert into orders values (?, ?, ?, ?)", (orderID, type, date, status))
        conn.commit()
    else:
        dateID = order[0]
        print("Date already exists, dateID is", dateID)


# Check if the pickup address exists, if does retrieve pickupID, if not create a new random pickupID
def check_pickup():
    global locationID
    curs.execute("select * from location where address = ?", (address,))
    pickup = curs.fetchone()
    if pickup is None:
        locationID = random.randint(100000, 999999)
        curs.execute("insert into location values (?, ?)", (locationID, address))
        conn.commit()
    else:
        locationID = pickup[0]
        print("Pickup already exists, pickupID is", locationID)


# Check if the destination address exists, if does retrieve dropoffID, if not create a new random dropoffID
def check_dropoff():
    global locationDropID
    curs.execute("select * from location where address = ?", (destination,))
    dropoff = curs.fetchone()
    if dropoff is None:
        locationDropID = random.randint(100000, 999999)
        curs.execute("insert into location values (?, ?)", (locationDropID, destination))
        conn.commit()
    else:
        locationDropID = dropoff[0]
        print("Dropoff already exists, dropoffID is", locationDropID)


# Lists the customer's name and payment

# result = curs.fetchall()
# print(result)


def create_new_order():
    
    check_customer()
    check_payment()
    check_order()
    check_pickup()
    check_dropoff()
    
    paysID = random.randint(100000, 999999)
    curs.execute("insert into pays values (?, ?, ?)", (paysID, customerID, paymentID))
    
    makesID = random.randint(100000, 999999)
    curs.execute("insert into makes values (?, ?, ?)", (makesID, customerID, orderID))
    
    hasID = random.randint(100000, 999999)
    curs.execute("insert into has values (?, ?, ?)", (hasID, orderID, paymentID))
    
    pickupID = random.randint(100000, 999999)
    curs.execute("insert into pickup values (?, ?, ?)", (pickupID, orderID, locationID))
    
    dropoffID = random.randint(100000, 999999)
    curs.execute("insert into dropoff values (?, ?, ?)", (dropoffID, orderID, locationDropID))

    conn.commit()


# Retrieve orders that have status 0
def incomplete():
    curs.execute(
    """
	SELECT customer.name, customer.phone,
	payment.paymentAmount, payment.tip, payment.total, payment.paymentType,
	orders.type, orders.date, orders.status,
	pick.address, ending.address
	FROM customer
            INNER JOIN pays ON customer.customerID = pays.customerID
            INNER JOIN payment ON pays.paymentID = payment.paymentID
            INNER JOIN makes ON customer.customerID = makes.customerID
            INNER JOIN orders ON makes.orderID = orders.ordersID
            INNER JOIN pickup ON pickup.orderID = orders.ordersID
            INNER JOIN location pick ON pickup.locationID = pick.locationID
            INNER JOIN dropoff ON dropoff.orderID = orders.ordersID
            INNER JOIN location ending ON dropoff.locationID = ending.locationID
        WHERE orders.status = 0
    """)
    incomplete = curs.fetchall()
    return (incomplete)
    
# Todo:
# Generate statistics (probably sql statements)
def stats():
    Stats = ""
    # Total number of orders
    curs.execute("select count(*) from orders")
    total_orders = curs.fetchone()
    Stats += f"total_orders : {total_orders}\n"
    # Total number of orders that are complete
    curs.execute("select count(*) from orders where status = 1")
    complete_orders = curs.fetchone()
    Stats += f"complete_orders : {complete_orders}\n"
    # Total number of orders that are incomplete
    curs.execute("select count(*) from orders where status = 0")
    incomplete_orders = curs.fetchone()
    Stats += f"incomplete_orders : {incomplete_orders}\n"
    # Number of orders created today
    curs.execute("select count(*) from orders where date = date('now')") # not sure if this is correct
    today_orders = curs.fetchone()
    Stats += f"today_orders : {today_orders}\n"
    # Number of orders created this week
    # Total earnings
    curs.execute("select sum(total) from payment")
    total_earnings = curs.fetchone()
    Stats += f"total_earnings : {total_earnings}\n"
    # Average order tip
    curs.execute("select avg(tip) from payment")
    avg_tip = curs.fetchone()
    Stats += f"avg_tip : {avg_tip}\n"
    # Average order total
    curs.execute("select avg(total) from payment")
    avg_total = curs.fetchone()
    Stats += f"avg_total : {avg_total}\n"

    return Stats


# Todo: edit this.. make new joins, and add the headers
def retrieve_table():
    curs.execute(
    """
	SELECT customer.name, customer.phone,
	payment.paymentAmount, payment.tip, payment.total, payment.paymentType,
	orders.type, orders.date, orders.status,
	pick.address, ending.address
	FROM customer
            INNER JOIN pays ON customer.customerID = pays.customerID
            INNER JOIN payment ON pays.paymentID = payment.paymentID
            INNER JOIN makes ON customer.customerID = makes.customerID
            INNER JOIN orders ON makes.orderID = orders.ordersID
            INNER JOIN pickup ON pickup.orderID = orders.ordersID
            INNER JOIN location pick ON pickup.locationID = pick.locationID
            INNER JOIN dropoff ON dropoff.orderID = orders.ordersID
            INNER JOIN location ending ON dropoff.locationID = ending.locationID
    """)
    result = curs.fetchall()
    return (result)



# Todo:
# Navigation system: 1. Enter new order; 2. Retrieve incomplete orders; 3. See stats; 4. See whole table.
if __name__ == "__main__":
    print("Hello, user!")
    print("1. Enter new order; 2. Retrieve incomplete orders; 3. See stats; 4. See whole table.")
    action = input("Choose: ")
    if action == "1":
        create_new_order()
    elif action == "2":
        incomplete()
    elif action == "3":
        stats()
    elif action == "4":
        retrieve_table()
    else:
        print("Invalid input")
