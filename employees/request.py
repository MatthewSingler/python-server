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