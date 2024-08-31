Simple HTTP Server and Client
This project contains a simple implementation of an HTTP server and client using Python's socket module.

HTTP Client
The HTTP client sends a request to the server and prints the response.

Usage
Run the Client:

bash
Copy code
python client.py
Customize Request: Modify the send_request function call in client.py to change the HTTP method (e.g., GET, POST).

HTTP Server
The HTTP server listens for incoming connections and handles GET and POST requests.

Usage
Run the Server:

bash
Copy code
python server.py
Interact with the Server:

GET Request: Returns a simple HTML page saying "Hello, World!"
POST Request: Returns a page saying "POST request received!"
Other Requests: Returns a "Method Not Allowed" response.
Files
client.py: Contains the client code for sending HTTP requests.
server.py: Contains the server code for handling HTTP requests.
