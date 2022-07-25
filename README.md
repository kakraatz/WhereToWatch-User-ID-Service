# User ID Microservice

This microservice implements a socket server with a client function to produce unique ID's for login/registering an account on the Where To Watch application.

**How to request data**

* socket_server.py must be running on your desired host and port number.
* socket_client.py contains the microservice function where you can pass in a login and service string variable.
* Using the microservice function will send a request for an ID to the server.

**How to receive data**

* The server will receive the login and service strings that are sent from the client function.
* A numeric ID will be generated for the associated account.
* The server writes the data to a database (in this case we are using a text file for simplicity).
  - Ensure the path to logins.txt in socket_server.py is correct.
* The server will respond to the client with the data and a success message.
* The client then returns the data for the application administrator to use.
