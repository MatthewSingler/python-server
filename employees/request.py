EMPLOYEES = [
    {
        "id": 1,
        "name": "Jessica Younker",
        "address": "123 Street St.",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Zoe LeBlanc",
        "email": "123 Street Rd.",
        "locationId": 1
    },
    {
        "name": "Hannah Hall",
        "email": "123 Avenue St.",
        "id": 5,
        "locationId": 2
    },
    {
        "name": "Jenna Solis",
        "email": "123 Street Ave.",
        "id": 14,
        "locationId": 1
    },
    {
        "id": 15,
        "name": "Ryan Tanay",
        "email": "123 Road St.",
        "locationId": 2
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id +1
    employee["id"] = new_id

    EMPLOYEES.append(employee)
    return employee

#function to delete an employee takes an id as an argument
def delete_employee(id):
#set initial value of the employee_index to -1 to initialize it, or incase one isn't found?
    employee_index = -1
#iterate the employees list(dictionary) but use enumerate so we can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
#if the id of the employee equals the id being passed in then set the index equal to employee index instead of -1.
        if employee["id"] == id:
            employee_index = index
#if the id was found, it's in position zero or greater, then use pop to remove it from the list(dictionary)
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
