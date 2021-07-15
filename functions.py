import sqlite3
conn = sqlite3.connect("employee.db")
c = conn.cursor()

def show(query):
    listing = c.execute(query)
    search_results = listing.fetchall()
    if len(search_results) < 1:
        print("Currently none\n")
    else:
        for element in search_results:
            fullname = element[0] + " " + element[1]
            print("Name: %s" %fullname)
            print("Email: %s" %element[2])
            print("Pay: $%d" %element[3])
            print("Position: %s"%element[4])
            print("Detail: %s\n"%element[5])

def getInfo(position):
    fname = input("Enter the {}'s first name: ".format(position))
    lname = input("Enter the {}'s last name: ".format(position))
    pay = int(input(("Enter the {}'s pay: ".format(position))))
    return fname, lname, pay
    
def insert_emp(emp, position, detail):
    with conn:
        c.execute("INSERT INTO employees VALUES(:first, :last, :email, :pay, :position, :detail)", {'first':emp.first, 'last':emp.last, "email":emp.email, 'pay':emp.pay, "position":position, "detail":detail})

def getUpdateRemovalInfo(position):
    fname = input("Enter the {}'s first name: ".format(position))
    lname = input("Enter the {}'s last name: ".format(position))
    return fname, lname

def remove_emp(fname, lname, position):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last AND position = :position", {"first":fname, "last":lname, "position":position})

def update_pay(fname, lname, position, pay):
    with conn:
        c.execute("UPDATE employees SET pay = :pay WHERE first = :first AND last = :last AND position = :position", {'pay': pay, 'first': fname, 'last':lname, "position":position})
        
