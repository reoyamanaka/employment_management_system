from classes import Employee, Manager, Developer, Intern
import sqlite3

conn = sqlite3.connect("employee.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS employees (
            first TEXT,
            last TEXT,
            email TEXT,
            pay INTEGER,
            position TEXT,
            detail TEXT
            )""")

position_dict = {"1":"manager", "2":"developer", "3":"intern"}

def show(query):
    listing = c.execute(query)
    for element in listing:
        fullname = element[0] + " " + element[1]
        print("Name: %s" %fullname)
        print("Email: %s" %element[2])
        print("Pay: %d" %element[3])
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

def getRemovalInfo(position):
    fname = input("Enter the {}'s first name: ".format(position))
    lname = input("Enter the {}'s last name: ".format(position))
    return fname, lname

def remove_emp(fname, lname, position):
    with conn:
        c.execute("DELETE FROM employees WHERE first = :first AND last = :last AND position = :position", {"first":fname, "last":lname, "position":position})

while True:
    print("\nWelcome to Company R")
    print("\n---MAIN MENU---\n")
    print("Choose an option:")
    print("1 - View list of employees")
    print("2 - Add an employee")
    print("3 - Remove an employee")
    option = input()
    if option == "1":
        while True:
            print("---VIEWING MODE---") 
            print("1 - See full list of employees")
            print("2 - See full list of managers")
            print("3 - See full list of developers")
            print("4 - See full list of interns")
            print("5 - Go back to main menu")
            viewOption = input()
            
            if viewOption == "1":
                print("Showing list of all employees...\n")
                show("SELECT * FROM employees")
            elif viewOption == "2":
                print("Showing list of all managers...\n")
                show("SELECT * FROM employees WHERE position = 'manager'")
            elif viewOption == "3":
                print("Showing list of all developers...\n")
                show("SELECT * FROM employees WHERE position = 'developer'")
            elif viewOption == "4":
                print("Showing list of all interns...\n")
                show("SELECT * FROM employees WHERE position = 'intern'")
            elif viewOption == "5":
                print("Returning to main menu...\n")
                break
            else:
                print("Invalid option.\n")
                             
    elif option == "2":
        print("---ADDING MODE---")
        print("1 - Add a manager")
        print("2 - Add a developer")
        print("3 - Add an intern")
        print("4 - Go back to previous menu")
        addOption = input()
        while True:
            if addOption == "1" or addOption == "2" or addOption == "3" or addOption == "4":
                position = position_dict[addOption]
                fname, lname, pay = getInfo(position)
                if addOption == "1":
                    detail = int(input("Enter manager's office ID: "))
                    new_manager = Manager(fname, lname, pay, detail)
                    insert_emp(new_manager, position, "Office ID = {}".format(detail))

                elif addOption == "2":
                    detail = input("Enter the developer's primary programming language: ")
                    new_developer = Developer(fname, lname, pay, detail)
                    insert_emp(new_developer, position, "Primary programming language = {}".format(detail))
                
                elif addOption == "3":
                    detail = input("Enter the intern's school: ")
                    new_intern = Intern(fname, lname, pay, detail)
                    insert_emp(new_intern, position, "School = {}".format(detail))
                
                elif addOption == "4":
                    print("Returning to previous menu...\n")
            else:
                print("Invalid option.\n")
            break
                 
    elif option == "3":
        print("---REMOVING MODE---")  
        print("1 - Remove a manager")
        print("2 - Remove a developer")
        print("3 - Remove an intern")
        print("4 - Go back to previous menu")
        removeOption = input()
        while True:
            if removeOption == "1" or removeOption == "2" or removeOption == "3" or removeOption == "4":
                position = position_dict[removeOption]
                fname, lname = getRemovalInfo(position)
                if removeOption == "4":
                    print("Returning to previous menu...\n")
                    break
                remove_emp(fname, lname, position)
                break
    else:
        print("Invalid option.\n")
