import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from customers import get_all_customers, get_single_customer, create_customer, delete_customer, update_customer
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location



# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions thats
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    # This is a Docstring it should be at the beginning of all classes and functions
    # It gives a description of the class or function
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple


    # Here's a class function
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        """Handles GET requests to the server
        """
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}

        (resource, id) = self.parse_url(self.path)

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"

            else:
                response = f"{get_all_animals()}"

        if resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"

            else:
                response = f"{get_all_locations()}"

        if resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"

            else:
                response = f"{get_all_employees()}"

        if resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"

            else:
                response = f"{get_all_customers()}"

        # Your new console.log() that outputs to the terminal
        #print(self.path)

        # It's an if..else statement
        #if self.path == "/animals":
            # In Python, this is a list of dictionaries
            # In JavaScript, you would call it an array of objects
            #response = get_all_animals()
        #else:
            #response = []

        # This weird code sends a response back to the client
        self.wfile.write(f"{response}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        """Handles POST requests to the server
        """
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)

        new_animal = None
        if resource == "animals":
            new_animal = create_animal(post_body)
            self.wfile.write(f"{new_animal}".encode())

        new_location = None
        if resource == "locations":
            new_location = create_location(post_body)
            self.wfile.write(f"{new_location}".encode())

        new_employee = None
        if resource == "employees":
            new_employee = create_employee(post_body)
            self.wfile.write(f"{new_employee}".encode())

        new_customer = None
        if resource == "customers":
            new_customer = create_customer(post_body)
            self.wfile.write(f"{new_customer}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        """Handles PUT requests to the server
        """
        self.do_POST()
#set a 204 response code. This is not going to return anything from server except a 204 response saying the action was performed
    def do_DELETE(self):
        self._set_headers(204)
#parse the url. The resource and id are a tuple that will be unpacked.
        (resource, id) = self.parse_url(self.path)
#delete a single animal fro the list. If the resource is animals, we run the delete function and it takes an id as an argument.
        if resource == "animals":
            delete_animal(id)
            self.wfile.write("".encode())

        if resource == "locations":
            delete_location(id)
            self.wfile.write("".encode())

        if resource == "employees":
            delete_employee(id)
            self.wfile.write("".encode())

        if resource == "customers":
            delete_customer(id)
            self.wfile.write("".encode())

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)

    # Encode the new animal and send in response
        self.wfile.write("".encode())

        if resource == "locations":
            update_location(id, post_body)
        self.wfile.write("".encode())

        if resource =="employees":
            update_employee(id, post_body)
        self.wfile.write("".encode())

        if resource == "customers":
            update_customer(id, post_body)
        self.wfile.write("".encode())
        

# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
