import sqlite3
import json
from sqlite3 import dbapi2
from models import Animal, Location, Customer

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "admitted"
    }
]


#def get_all_animals():
#    return ANIMALS
# Function with a single parameter


#def get_single_animal(id):
    # Variable to hold the found animal, if it exists
#    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
#    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
#        if animal["id"] == id:
#            requested_animal = animal

#    return requested_animal


def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    animal_index = -1
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            animal_index = index

    if animal_index >= 0:
        ANIMALS.pop(animal_index)


#def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
#    for index, animal in enumerate(ANIMALS):
#        if animal["id"] == id:
            # Found the animal. Update the value.
#            ANIMALS[index] = new_animal
#            break
def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Animal
        SET
            name = ?,
            breed = ?,
            status = ?,
            location_id = ?,
            customer_id = ?
        WHERE id = ?
        """, (  new_animal["name"],
                new_animal["breed"],
                new_animal["status"],
                new_animal["location_id"], 
                new_animal["customer_id"],
                id))
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
        a.id,
        a.name,
        a.breed,
        a.status,
        a.location_id,
        a.customer_id,
        l.name location_name,
        l.address location_address,
        c.name customer_name,
        c.address customer_address
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            location = Location(row['location_id'], row['location_name'], row['location_address'])
            animal.location = location.__dict__
            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'])
            animal.customer = customer.__dict__

            animals.append(animal.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'], data['status'], data['location_id'], data['customer_id'])

        return json.dumps(animal.__dict__)


def get_animal_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
        a.id,
        a.name,
        a.status,
        a.breed,
        a.location_id,
        a.customer_id
        FROM Animal a
        WHERE a.location_id = ?
        """, (location_id, ))

        animals = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['status'], row['breed'], row['location_id'], row['customer_id'])
            animals.append(animal.__dict__)

    return json.dumps(animals)

def get_animal_by_status(status):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
        a.id,
        a.name,
        a.status,
        a.breed,
        a.location_id,
        a.customer_id
        FROM Animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            animal = Animal(row["id"], row["name"], row["status"], row["breed"], row["location_id"], row["customer_id"])
            animals.append(animal.__dict__)
        return json.dumps(animals)

def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))
