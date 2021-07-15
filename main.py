from classes import Employee, Manager, Developer, Intern
import sqlite3
from functions import show, getInfo, insert_emp, getUpdateRemovalInfo, remove_emp, update_pay

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

while True:
    print("\nWelcome to the Employment Management System")
    print("\n---MAIN MENU---\n")
    print("Choose an option:")
    print("1 - View list of employees")
    print("2 - Add an employee")
    print("3 - Remove an employee")
    print("4 - Update pay")
    print("5 - Exit")
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
                if addOption == "4":
                    print("Returning to previous menu...\n")
                    break
                else:   
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
                if removeOption == "4":
                    print("Returning to previous menu...\n")
                    break
                position = position_dict[removeOption]
                fname, lname = getUpdateRemovalInfo(position)
                remove_emp(fname, lname, position)
                break
    elif option == "4":
        print("---UPDATE PAY MODE---")
        print("1 - Update pay of a manager")
        print("2 - Update pay of a developer")
        print("3 - Update pay of an intern")
        print("4 - Go back to previous menu")
        updateOption = input()
        while True:
            if updateOption == "1" or updateOption == "2" or updateOption == "3" or updateOption == "4":
                if updateOption == "4":
                    print("Returning to previous menu...\n")
                    break
                position = position_dict[updateOption]
                fname, lname = getUpdateRemovalInfo(position)
                new_pay = int(input("Enter new pay: "))
                update_pay(fname, lname, position, new_pay)
                break
            else:
                print("Invalid option.\n")
    elif option == "5":
        print("Exiting...\n")
        break
    else:
        print("Invalid option.\n")
