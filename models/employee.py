class Employee():
    def __init__(self, id, name, email, location_id = ""):
        self.id = id
        self.name = name
        self.email = email
        self.location_id = location_id
        self.location = None