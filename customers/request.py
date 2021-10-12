CUSTOMERS = [
    {
        "id": 1,
        "name": "Cassie Tesauro",
        "email": "cassie@tesauro.com",
        "password": "1234"
    },
    {
        "id": 2,
        "name": "Ben Gregory",
        "email": "ben@gregory.com",
        "password": "1234"
    },
    {
        "name": "Myriam Chevalier",
        "email": "myriam@chavalier.com",
        "password": "1234",
        "id": 3
    },
    {
        "name": "Matthew Singler",
        "email": "matthew@singler.com",
        "password": "1234",
        "id": 4
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer